import pypdf

def print_page_snippet(pdf_path, page_num):
    reader = pypdf.PdfReader(pdf_path)
    page = reader.pages[page_num - 1]
    t = page.extract_text()
    lines = t.splitlines()
    print(f"\n==========================================")
    print(f"FILE: {pdf_path} | PDF PAGE: {page_num}")
    print(f"==========================================")
    # find lines with iÙkk or gqde or vkns'k
    for i, line in enumerate(lines):
        if 'iÙkk' in line or 'gqde' in line or 'r:oj' in line or 'bPNk' in line:
            start = max(0, i-5)
            end = min(len(lines), i+6)
            for j in range(start, end):
                print(f"{j+1}: {lines[j]}")
            print("---")

print_page_snippet(r"रामपाल पाखंडी\books\gyan_ganga_hindi.pdf", 212)
print_page_snippet(r"रामपाल पाखंडी\books\muktibodh.pdf", 514)
print_page_snippet(r"रामपाल पाखंडी\books\garima-gita-ki.pdf", 147)
print_page_snippet(r"रामपाल पाखंडी\books\garima-gita-ki.pdf", 256)
print_page_snippet(r"रामपाल पाखंडी\books\kabir-bada-ya-krishna.pdf", 221)
