import pypdf

baran_path = r"C:\Kiến thức cần học\CRM\references\Roger J. Baran  Robert J. Galka - Customer Relationship Management (0).pdf"
fund_path = r"C:\Kiến thức cần học\CRM\references\CRM-Fundamentals.pdf"

baran_reader = pypdf.PdfReader(baran_path)
fund_reader = pypdf.PdfReader(fund_path)

def sample_baran(ch_start, ch_end, title):
    text = ""
    for p in range(ch_start, ch_end):
        text += baran_reader.pages[p].extract_text() + "\n"
    print(f"=== BARAN {title} (Pages {ch_start+1}-{ch_end}) ===")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    for l in lines[:25]:
        print("  ", l)

def sample_fund(ch_start, ch_end, title):
    text = ""
    for p in range(ch_start, ch_end):
        text += fund_reader.pages[p].extract_text() + "\n"
    print(f"\n=== FUNDAMENTALS {title} (Pages {ch_start+1}-{ch_end}) ===")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    for l in lines[:25]:
        print("  ", l)

# Baran Ch 5: p. 140 (idx 139) to 179 (idx 179)
sample_baran(139, 145, "Chapter 5: CRM and Data Management")
# Baran Ch 6: p. 180 (idx 179) to 207 (idx 207)
sample_baran(179, 185, "Chapter 6: Technology and Data Platforms")
# Baran Ch 7: p. 208 (idx 207) to 238 (idx 238)
sample_baran(207, 213, "Chapter 7: Database and Customer Data Development")

# Fund Ch 3: p. 61 (idx 60) to 76 (idx 76)
sample_fund(60, 66, "Chapter 3: Building a CRM Roadmap")
# Fund Ch 4: p. 77 (idx 76) to 104 (idx 104)
sample_fund(76, 82, "Chapter 4: Evaluating Software and Consultants")
