import pypdf
import os

pdf_path = r"रामपाल पाखंडी\books\kabir-sagar-ka-sarlarth.pdf"
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages in kabir-sagar-ka-sarlarth.pdf: {len(reader.pages)}")

# Let's search for interesting words in KrutiDev
targets = {
    'lqUur': 'सुन्नत',
    'fyax': 'लिंग',
    ';ksfu': 'योनि',
    'uk[kwu': 'नाखून',
    'cykRdkj': 'बलात्कार',
    'oh;Z': 'वीर्य',
    'dekyh': 'कमाली',
    'dekY': 'कमाल',
    'yksbZ': 'लोई',
    "os';k": 'वेश्या',
    'xkf.kdk': 'गणिका',
    "is'kkc": 'पेशाब',
    'Hkx': 'भग'
}

results = {k: [] for k in targets}

for p_idx, page in enumerate(reader.pages):
    t = page.extract_text()
    for k in targets:
        if k in t:
            results[k].append(p_idx + 1)

for k, pages in results.items():
    print(f"Target '{targets[k]}' ({k}): found in {len(pages)} pages -> {pages[:15]}")
