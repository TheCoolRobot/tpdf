"""Multi-page document example"""

from tpdf import TPDF

# Create multi-page document
doc = TPDF(multipage=True)

# Cover page
doc.add_page(background='#f0f9ff')
doc.add_text('Annual Report 2025', 306, 350, 
             fontSize=42, fontWeight='bold', color='#1e40af')
doc.add_text('Company Name', 306, 400,
             fontSize=20, color='#64748b')

# Table of contents
doc.add_page()
doc.add_text('Table of Contents', 50, 60,
             fontSize=28, fontWeight='bold')
doc.add_text('1. Executive Summary ........... 3', 50, 110, fontSize=14)
doc.add_text('2. Financial Overview ........... 4', 50, 135, fontSize=14)
doc.add_text('3. Future Outlook .............. 5', 50, 160, fontSize=14)

# Executive summary
doc.add_page()
doc.add_text('Executive Summary', 50, 60,
             fontSize=28, fontWeight='bold', color='#1e40af')
doc.add_text('This year showed strong growth...', 50, 110, fontSize=12)

# Generate PDF
doc.compile_to_pdf('multipage_example.pdf')

print("✅ Created multipage_example.pdf (3 pages)")