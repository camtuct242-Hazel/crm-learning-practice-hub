import pypdf

baran_path = r"C:\Kiến thức cần học\CRM\references\Roger J. Baran  Robert J. Galka - Customer Relationship Management (0).pdf"
fund_path = r"C:\Kiến thức cần học\CRM\references\CRM-Fundamentals.pdf"

baran_reader = pypdf.PdfReader(baran_path)
fund_reader = pypdf.PdfReader(fund_path)

def check_ch(reader, pstart, pend, label):
    txt = ""
    for p in range(pstart, pend):
        txt += reader.pages[p].extract_text() + "\n"
    lines = [l.strip() for l in txt.split("\n") if l.strip()]
    print(f"*** {label} (p.{pstart+1}-{pend}) ***")
    for l in lines[:15]:
        print("  ", l)

check_ch(baran_reader, 238, 243, "Baran Ch 8 (B2B CRM)")
check_ch(baran_reader, 269, 274, "Baran Ch 9 (Profit Chain)")
check_ch(baran_reader, 295, 300, "Baran Ch 10 (Acquisition/Retention/Win-Back)")
check_ch(baran_reader, 316, 321, "Baran Ch 11 (Privacy & Ethics)")
check_ch(baran_reader, 351, 356, "Baran Ch 12 (Measurement & Tools)")
check_ch(baran_reader, 397, 402, "Baran Ch 13 (Social Networking & CRM)")
check_ch(baran_reader, 430, 435, "Baran Ch 14 (Trends, Challenges & Opportunities)")

check_ch(fund_reader, 104, 109, "Fund Ch 5 (Planning Initial Implementation)")
check_ch(fund_reader, 141, 146, "Fund Ch 6 (Executing Initial Implementation)")
check_ch(fund_reader, 207, 212, "Fund Ch 7 (Maintaining & Evolving CRM)")
