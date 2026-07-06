#!/usr/bin/env python3
"""
ColdCaseIndex — default Open Graph image generator (1200x630).
Dark background with the site logo mark, name, and tagline.
Run from the project root: python3 scripts/generate_og_image.py
"""

import os

from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
OUT_FILE = os.path.join(ROOT_DIR, 'og-image.png')
LOGO_FILE = os.path.join(ROOT_DIR, 'logos', 'logo-icon-256x256.png')

W, H = 1200, 630
BG = (15, 23, 42)          # slate-900, matches manifest background_color
BG_GLOW = (30, 41, 82)
ACCENT = (99, 102, 241)    # indigo, matches theme_color #6366f1
TEXT = (241, 245, 249)
MUTED = (148, 163, 184)


def load_font(size, bold=False):
    candidates = [
        '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf',
        '/System/Library/Fonts/Helvetica.ttc',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default(size)


def main():
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    # soft radial glow, top center
    glow = Image.new('L', (W, H), 0)
    gdraw = ImageDraw.Draw(glow)
    for r in range(500, 0, -8):
        alpha = int(50 * (1 - r / 500))
        gdraw.ellipse([W // 2 - r * 1.4, -r, W // 2 + r * 1.4, r], fill=alpha)
    img.paste(Image.new('RGB', (W, H), BG_GLOW), (0, 0), glow)
    draw = ImageDraw.Draw(img)

    # accent rule
    draw.rectangle([0, H - 10, W, H], fill=ACCENT)

    # logo mark
    text_left = 90
    if os.path.exists(LOGO_FILE):
        logo = Image.open(LOGO_FILE).convert('RGBA').resize((140, 140), Image.LANCZOS)
        img.paste(logo, (90, 150), logo)
        text_left = 262

    # site name + tagline
    draw.text((text_left, 158), 'ColdCaseIndex', font=load_font(84, bold=True), fill=TEXT)
    draw.text((text_left, 268), 'Cold Case & Historic Crime Database', font=load_font(38), fill=ACCENT)

    draw.text((90, 400), 'Documented cold cases, missing persons, and historic', font=load_font(34), fill=MUTED)
    draw.text((90, 448), 'crimes across all 50 states — from the 1890s to today.', font=load_font(34), fill=MUTED)
    draw.text((90, 540), 'coldcaseindex.com', font=load_font(30), fill=MUTED)

    img.save(OUT_FILE, 'PNG', optimize=True)
    print(f"Wrote {OUT_FILE} ({os.path.getsize(OUT_FILE) // 1024} KB)")


if __name__ == '__main__':
    main()
