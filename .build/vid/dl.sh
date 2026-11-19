#!/bin/bash
cd /home/user/.build/vid
python3 - <<'PY' > list.txt
import json
d=json.load(open("picks.json"))
for n,(vid,st) in sorted(d.items(),key=lambda x:int(x[0])):
    print(n,vid,st)
PY
while read n vid st; do
  if [ -s "raw_$n.mp4" ]; then echo "skip $n"; continue; fi
  end=$((st+8))
  yt-dlp -q --no-warnings --force-keyframes-at-cuts \
    -f "bestvideo[height<=720][vcodec^=avc1]/bestvideo[height<=720]/best[height<=720]" \
    --download-sections "*${st}-${end}" --merge-output-format mp4 \
    -o "raw_$n.%(ext)s" "https://www.youtube.com/watch?v=$vid" 2>err_$n.txt
  echo "$n -> $(ls -la raw_$n.mp4 2>/dev/null | awk '{print $5}') $(head -c 120 err_$n.txt)"
done < list.txt
