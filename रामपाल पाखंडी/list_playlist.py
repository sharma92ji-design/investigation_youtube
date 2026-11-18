import subprocess
import json
import os

playlist_url = "https://www.youtube.com/playlist?list=PLbsKPTQZinaY"
cmd = ["yt-dlp", "--flat-playlist", "--dump-single-json", playlist_url]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

data = json.loads(res.stdout)
title = data.get("title", "")
entries = data.get("entries", [])

print(f"Playlist Title: {title}")
print(f"Total Videos: {len(entries)}\n")

out_lines = [f"# Playlist: {title}", f"Total Videos: {len(entries)}\n"]

for i, e in enumerate(entries, 1):
    vid_id = e.get("id")
    v_title = e.get("title")
    dur_sec = e.get("duration") or 0
    dur_min = round(dur_sec / 60, 1)
    line = f"{i}. [{vid_id}] ({dur_min} min) {v_title}"
    print(line)
    out_lines.append(f"{i}. [{v_title}](https://www.youtube.com/watch?v={vid_id}) - {dur_min} min (ID: `{vid_id}`)")

out_path = r"I:\Sanjeev Kumar Sharma\Shwetank Flocky Ji Pandey\Sritantu\projects-2027\investigation_youtube\रामपाल पाखंडी\sources\playlist_videos.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print(f"\nSaved playlist metadata to: {out_path}")

