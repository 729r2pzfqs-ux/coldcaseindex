#!/bin/bash
cd "$(dirname "$0")"
rm -f .git/index.lock
git add -A
git commit -m "fix: add license field to Dataset structured data

Adds Creative Commons BY-NC 4.0 license to Dataset JSON-LD
to resolve GSC 'missing field license' warning.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
git push
