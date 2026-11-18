import pypdf

reader = pypdf.PdfReader(r"रामपाल पाखंडी\books\kabir-sagar-ka-sarlarth.pdf")

pages_to_check = {
    'linga': [170, 402, 490, 537],
    'balatkar': [173, 253, 286, 357, 641, 674],
    'virya': [357, 374, 455, 526, 650, 658],
    'peshab': [377, 378, 514, 537],
    'weshya': [271],
    'nakhun': [297, 372, 620],
    'loi': [22, 97, 137, 160, 230, 315, 408, 675],
    'kamali': [9, 100, 101, 302, 349, 487, 536, 538, 554, 555, 565, 566]
}

all_pages = sorted(list(set([p for sub in pages_to_check.values() for p in sub])))

for p in all_pages:
    text = reader.pages[p-1].extract_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    header = lines[0] if lines else ""
    footer = lines[-1] if lines else ""
    print(f"\n==================== PDF PAGE {p} ====================")
    print(f"Header: {header} | Footer: {footer}")
    # print relevant lines
    for line in lines:
        for k in ['lqUur', 'fyax', 'cykRdkj', 'oh;Z', 'is\'kkc', "os';k", 'uk[kwu', 'yksbZ', 'dekyh']:
            if k in line:
                print(f"  [{k}]: {line}")
                break
