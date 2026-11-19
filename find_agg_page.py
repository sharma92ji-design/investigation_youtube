import pypdf

reader = pypdf.PdfReader(r"रामपाल पाखंडी\books\adhyatmik_gyan_ganga.pdf")
print("Searching adhyatmik_gyan_ganga.pdf...")
target_found = False
for idx, page in enumerate(reader.pages):
    t = page.extract_text()
    if 'iÙkk Hkh ugha fgy ldrk' in t or 'ftldh vkKk fcuk' in t or 'jksxh dks LoLFk djs' in t:
        print(f"Found on PDF page {idx+1}")
        for l in t.splitlines()[:25]:
            print("  ", l)
        target_found = True
        break

if not target_found:
    print("Exact phrase not in adhyatmik_gyan_ganga.pdf, let's search for similar phrases")
    for idx, page in enumerate(reader.pages):
        t = page.extract_text()
        if 'bPNk' in t and 'fcuk' in t and 'dchj' in t:
            print(f"Page {idx+1} has bPNk + fcuk + dchj")
