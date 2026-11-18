import os
import re
import sys
import time
import subprocess
import glob

VIDEO_IDS = [
    "kRnaa5XcQQk",
    "jaLzR0wa8Xk",
    "5KtuV9xp8SY",
    "t1GJbehHBZk",
    "_TZ9x8_Aue4",
    "yMPdW6MLKtQ",
    "YT2d2V4fadU",
    "J-srWWmSi24",
    "YoYz3SAqQEM",
    "sSz7Nx2x1gE",
    "roHxkVUlLgU",
    "O5RZ1JBUnP0",
    "jmLGwrR036o",
    "vTrDjm-wg9s"
]

TRANSCRIPTS_DIR = r"I:\Sanjeev Kumar Sharma\Shwetank Flocky Ji Pandey\Sritantu\projects-2027\investigation_youtube\रामपाल पाखंडी\transcripts"

def srt_to_readable(srt_path, readable_path):
    if not os.path.exists(srt_path):
        return False
    with open(srt_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    blocks = content.strip().split("\n\n")
    out_lines = []
    prev_text = ""

    time_re = re.compile(r"(\d{2}:\d{2}:\d{2}),\d{3}\s*-->\s*(\d{2}:\d{2}:\d{2}),\d{3}")

    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 2:
            continue
        # Find the line with the timestamp
        timestamp_line_idx = -1
        match = None
        for idx, line in enumerate(lines):
            m = time_re.search(line)
            if m:
                match = m
                timestamp_line_idx = idx
                break

        if not match or timestamp_line_idx == -1:
            continue

        start_time = match.group(1)
        text_lines = lines[timestamp_line_idx + 1:]
        text = " ".join(text_lines).strip()

        if text and text != prev_text:
            out_lines.append(f"[{start_time}] {text}")
            prev_text = text

    with open(readable_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print(f"Created readable transcript: {os.path.basename(readable_path)} ({len(out_lines)} lines)")
    return True

def process_all():
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

    for idx, vid_id in enumerate(VIDEO_IDS, 1):
        print(f"\n[{idx}/{len(VIDEO_IDS)}] Processing video ID: {vid_id}...")

        # Check if srt already exists for this video ID
        existing_srts = glob.glob(os.path.join(TRANSCRIPTS_DIR, f"*{vid_id}*.hi.srt"))
        
        if existing_srts:
            srt_file = existing_srts[0]
            print(f"SRT already exists: {os.path.basename(srt_file)}")
        else:
            url = f"https://www.youtube.com/watch?v={vid_id}"
            out_template = os.path.join(TRANSCRIPTS_DIR, "%(title)s [%(id)s].%(ext)s")
            cmd = [
                "yt-dlp",
                "--write-sub",
                "--write-auto-sub",
                "--sub-lang", "hi",
                "--sub-format", "srt",
                "--skip-download",
                "-o", out_template,
                url
            ]
            print(f"Downloading subtitle via yt-dlp...")
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
            if res.returncode != 0:
                print(f"yt-dlp stderr: {res.stderr[:300]}")
            
            existing_srts = glob.glob(os.path.join(TRANSCRIPTS_DIR, f"*{vid_id}*.hi.srt"))
            if existing_srts:
                srt_file = existing_srts[0]
                print(f"Downloaded: {os.path.basename(srt_file)}")
            else:
                print(f"WARNING: Could not find downloaded SRT for {vid_id}")
                continue

        # Convert to readable txt
        readable_file = srt_file.replace(".hi.srt", ".hi_readable.txt")
        if not os.path.exists(readable_file) or os.path.getsize(readable_file) == 0:
            srt_to_readable(srt_file, readable_file)
        else:
            print(f"Readable file already exists: {os.path.basename(readable_file)}")

        time.sleep(1)

    print("\n================== ALL DONE ==================")

if __name__ == "__main__":
    process_all()

