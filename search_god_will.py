import os, glob, pypdf

def safe_path(p):
    ap = os.path.abspath(p)
    if os.name == 'nt' and not ap.startswith('\\\\?\\'):
        return '\\\\?\\' + ap
    return ap

# Keywords in KrutiDev
# Let's search books first, and then transcripts
print("=== SEARCHING ALL PDF BOOKS ===")
books = glob.glob(r"रामपाल पाखंडी\books\*.pdf")
for b in books:
    bname = os.path.basename(b)
    try:
        reader = pypdf.PdfReader(safe_path(b))
        for p_idx, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue
            
            # Let's check for "iÙkk" (पत्ता)
            if 'iÙkk' in text:
                pos = 0
                while True:
                    pos = text.find('iÙkk', pos)
                    if pos == -1: break
                    snippet = text[max(0, pos-80):min(len(text), pos+120)].replace('\n', ' ')
                    print(f"[{bname} P.{p_idx+1}] Matched 'iÙkk' (पत्ता): {snippet}")
                    pos += 4
            
            # Check for "bPNk" (इच्छा) near "ijekRek" (परमात्मा) or "dchj" (कबीर) or "Hkxoku" (भगवान)
            if 'bPNk' in text and ('ijekRek' in text or 'dchj' in text or 'Hkxoku' in text):
                pos = 0
                while True:
                    pos = text.find('bPNk', pos)
                    if pos == -1: break
                    snippet = text[max(0, pos-80):min(len(text), pos+120)].replace('\n', ' ')
                    if any(w in snippet for w in ['ijekRek', 'dchj', 'Hkxoku', 'fcuk', 'dky']):
                        print(f"[{bname} P.{p_idx+1}] Matched 'bPNk' (इच्छा): {snippet}")
                    pos += 4

            # Check for "ethZ" (मर्जी)
            if 'ethZ' in text:
                pos = 0
                while True:
                    pos = text.find('ethZ', pos)
                    if pos == -1: break
                    snippet = text[max(0, pos-80):min(len(text), pos+120)].replace('\n', ' ')
                    print(f"[{bname} P.{p_idx+1}] Matched 'ethZ' (मर्जी): {snippet}")
                    pos += 4

            # Check for Unicode (in case PDF has unicode)
            if 'इच्छा' in text and ('परमात्मा' in text or 'कबीर' in text or 'भगवान' in text):
                pos = 0
                while True:
                    pos = text.find('इच्छा', pos)
                    if pos == -1: break
                    snippet = text[max(0, pos-80):min(len(text), pos+120)].replace('\n', ' ')
                    print(f"[{bname} P.{p_idx+1}] Matched Unicode 'इच्छा': {snippet}")
                    pos += 5

            if 'पत्ता' in text:
                pos = 0
                while True:
                    pos = text.find('पत्ता', pos)
                    if pos == -1: break
                    snippet = text[max(0, pos-80):min(len(text), pos+120)].replace('\n', ' ')
                    print(f"[{bname} P.{p_idx+1}] Matched Unicode 'पत्ता': {snippet}")
                    pos += 5

    except Exception as e:
        print(f"Error reading {bname}: {e}")

print("\n=== SEARCHING TRANSCRIPTS (SRT / TXT) ===")
transcripts = glob.glob(r"रामपाल पाखंडी\transcripts\livekistrampalpakhand\**\*.txt", recursive=True)
for tr in transcripts:
    fname = os.path.basename(tr)
    try:
        with open(safe_path(tr), 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for l_no, line in enumerate(lines, 1):
            for ut in ['पत्ता भी', 'पत्ता नहीं', 'परमात्मा की इच्छा', 'कबीर की इच्छा', 'भगवान की इच्छा', 'प्रभु की इच्छा', 'की मर्जी', 'इच्छा के बिना', 'इच्छा से ही', 'मर्जी के बिना']:
                if ut in line:
                    print(f"[{fname}:{l_no}] ({ut}) -> {line.strip()[:150]}")
    except Exception as e:
        print(f"Error reading transcript {fname}: {e}")
