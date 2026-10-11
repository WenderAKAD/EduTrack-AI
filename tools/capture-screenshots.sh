#!/usr/bin/env bash
# Capture page screenshots of the EduTrack AI shell at phone and browser widths,
# using Chrome headless with SwiftShader (software WebGL) — the hardware cannot
# do GPU-accelerated rendering. Usage: ./tools/capture-screenshots.sh
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE="http://127.0.0.1:8080"
OUT="docs/evidencias/tarefa09"
mkdir -p "$OUT"

pages=("home:390,844" "home:1280,800" "subjects:390,844" "subjects:1280,800" "tasks:390,844" "tasks:1280,800")

for spec in "${pages[@]}"; do
  page="${spec%%:*}"
  size="${spec##*:}"
  name="flutterflow-${page}-${size%%x*}.png"
  if [ "$size" = "390,844" ]; then
    name="flutterflow-${page}-phone.png"
  else
    name="flutterflow-${page}-browser.png"
  fi
  url="$BASE/?page=$page"
  echo "capturing $name ($size) <- $url"
  "$CHROME" --headless=new --disable-gpu --enable-unsafe-swiftshader \
    --use-angle=swiftshader --hide-scrollbars \
    --window-size="$size" --force-device-scale-factor=1 \
    --virtual-time-budget=30000 \
    --screenshot="$OUT/$name" "$url" 2>/dev/null || true
  sleep 1
done

ls -la "$OUT"
echo "DONE"