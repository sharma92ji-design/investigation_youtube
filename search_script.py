import os
import pypdf

reader = pypdf.PdfReader(r"रामपाल पाखंडी\books\KARONTHA KAND KA RAHASY.pdf")
keywords = ['lhMh', '[khj', 'd.kM', 'xHkZ', 'Luku', "v'yhy", 'L=kh', 'cykRdkj', 'O;fHkpkj', 'vkjksi', 'nhi', 'djkSaFkk']

print(f"Total pages: {len(reader.pages)}")
for idx, page in enumerate(reader.pages):
    t = page.extract_text()
    matched = [k for k in keywords if k in t]
    if matched:
        print(f"\n=== Page {idx+1} (Matched: {matched}) ===")
        for m in matched:
            pos = 0
            while True:
                pos = t.find(m, pos)
                if pos == -1:
                    break
                start = max(0, pos - 60)
                end = min(len(t), pos + 120)
                print(f"  [{m}]: {t[start:end].replace(chr(10), ' ')}")
                pos += len(m) + 10
