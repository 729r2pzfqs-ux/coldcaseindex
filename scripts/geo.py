#!/usr/bin/env python3
"""
Geometry for the /map/ explorer.

project(lon, lat)  -> (x, y) in the 975 x 610 viewBox of the pre-projected us-atlas
                      state outlines (d3's geoAlbersUsa at scale 1300, translate
                      487.5, 305), or None for points outside the three insets.
load_states()      -> {abbr: svg_path} read from data/us-states-albers.json.

To regenerate the outlines from us-atlas (TopoJSON, pre-projected):
    curl -O https://cdn.jsdelivr.net/npm/us-atlas@3/states-albers-10m.json
    python3 scripts/geo.py path/to/states-albers-10m.json
The arcs are simplified (Douglas-Peucker, 0.6px) before assembly so shared borders
still coincide. `--check` projects a few known cities and confirms each falls inside
its state's outline.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import viz  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATES_FILE = os.path.join(ROOT, 'data', 'us-states-albers.json')
W, H = 975, 610
SCALE, TX, TY = 1300, 487.5, 305
RAD = math.pi / 180


def _conic_equal_area(p0, p1, rotate_lon, center, scale, translate):
    """A d3 conicEqualArea projection with rotate([rotate_lon, 0]), center, scale and translate."""
    y0, y1 = p0 * RAD, p1 * RAD
    sy0 = math.sin(y0)
    n = (sy0 + math.sin(y1)) / 2
    c = 1 + sy0 * (2 * n - sy0)
    r0 = math.sqrt(c) / n

    def raw(lam, phi):
        r = math.sqrt(c - 2 * n * math.sin(phi)) / n
        return r * math.sin(lam * n), r0 - r * math.cos(lam * n)

    cx, cy = raw(center[0] * RAD, center[1] * RAD)
    tx, ty = translate

    def project(lon, lat):
        lam = lon + rotate_lon
        lam = ((lam + 180) % 360) - 180
        px, py = raw(lam * RAD, lat * RAD)
        return tx + scale * (px - cx), ty - scale * (py - cy)
    return project


_lower48 = _conic_equal_area(29.5, 45.5, 96, (-0.6, 38.7), SCALE, (TX, TY))
_alaska = _conic_equal_area(55, 65, 154, (-2, 58.5), SCALE * 0.35, (TX - 0.307 * SCALE, TY + 0.201 * SCALE))
_hawaii = _conic_equal_area(8, 18, 157, (-3, 19.9), SCALE, (TX - 0.205 * SCALE, TY + 0.212 * SCALE))


def project(lon, lat):
    if lat >= 50 and (lon < -128 or lon > 170):
        x, y = _alaska(lon, lat)
    elif 18 <= lat <= 23 and -161 <= lon <= -154:
        x, y = _hawaii(lon, lat)
    else:
        x, y = _lower48(lon, lat)
    if not (0 <= x <= W and 0 <= y <= H):
        return None
    return round(x, 1), round(y, 1)


def load_states():
    with open(STATES_FILE, encoding='utf-8') as f:
        return json.load(f)['states']


# ─────────────────────────── regeneration from TopoJSON ───────────────────────────

def _decode_arcs(topo):
    sx, sy = topo['transform']['scale']
    tx, ty = topo['transform']['translate']
    out = []
    for arc in topo['arcs']:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sx + tx, y * sy + ty))
        out.append(pts)
    return out


def _simplify(pts, tol):
    """Douglas-Peucker, iterative."""
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = pts[a]
        bx, by = pts[b]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        best, bi = 0.0, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            d = abs(dy * px - dx * py + bx * ay - by * ax) / L if L else math.hypot(px - ax, py - ay)
            if d > best:
                best, bi = d, i
        if best > tol:
            keep[bi] = True
            stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def _ring(arc_ids, arcs):
    pts = []
    for i in arc_ids:
        seg = arcs[i] if i >= 0 else list(reversed(arcs[~i]))
        if pts and pts[-1] == seg[0]:
            seg = seg[1:]
        pts.extend(seg)
    return pts


def _path(rings):
    parts = []
    for ring in rings:
        if len(ring) < 4:
            continue
        parts.append('M' + ' '.join(f'{x:.1f} {y:.1f}' for x, y in ring[:-1]) + 'Z')
    return ''.join(parts)


def build(topo_path, tol=0.6):
    with open(topo_path, encoding='utf-8') as f:
        topo = json.load(f)
    arcs = [_simplify(a, tol) for a in _decode_arcs(topo)]
    states = {}
    for g in topo['objects']['states']['geometries']:
        name = g['properties']['name']
        ab = viz.STATE_ABBR.get(name)
        if not ab:
            continue
        polys = g['arcs'] if g['type'] == 'MultiPolygon' else [g['arcs']]
        rings = [_ring(r, arcs) for poly in polys for r in poly]
        states[ab] = _path(rings)
    with open(STATES_FILE, 'w', encoding='utf-8') as f:
        json.dump({'source': 'us-atlas@3 states-albers-10m.json, simplified', 'viewBox': [W, H],
                   'states': states}, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')
    return states


def _inside(path, x, y):
    """Ray casting over every subpath of a path written by _path()."""
    inside = False
    for sub in path.split('Z'):
        if not sub.startswith('M'):
            continue
        nums = [float(v) for v in sub[1:].split()]
        pts = list(zip(nums[0::2], nums[1::2]))
        n = len(pts)
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % n]
            if (y1 > y) != (y2 > y):
                xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if x < xi:
                    inside = not inside
    return inside


CHECKS = [('CA', -118.24, 34.05), ('NY', -74.01, 40.71), ('AK', -149.9, 61.22), ('HI', -157.86, 21.31),
          ('FL', -80.19, 25.76), ('WA', -122.33, 47.6), ('IL', -87.63, 41.88), ('TX', -95.37, 29.76),
          ('ME', -70.25, 43.66), ('MT', -113.99, 46.87), ('DC', -77.04, 38.9)]


def check():
    states = load_states()
    bad = 0
    for ab, lon, lat in CHECKS:
        pt = project(lon, lat)
        ok = bool(pt) and _inside(states[ab], *pt)
        bad += not ok
        print(f'{ab}: {pt} {"ok" if ok else "OUTSIDE"}')
    return bad


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(1 if check() else 0)
    if len(sys.argv) > 1:
        s = build(sys.argv[1])
        print(f'wrote {len(s)} state outlines, {os.path.getsize(STATES_FILE):,} bytes')
