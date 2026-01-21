"""Text alignment and wrapping example"""

from tpdf import TPDF

# Create document
doc = TPDF()

# Centered title
doc.center('TPDF Alignment Demo', 50, fontSize=28, fontWeight='bold', color='#1e40af')

# Left aligned text
doc.left('This is left-aligned text', 100, fontSize=14)

# Right aligned text
doc.right('This is right-aligned text', 130, fontSize=14)

# Centered text
doc.center('This is centered text', 160, fontSize=14, color='#059669')

# Paragraph with auto-wrapping
long_text = "This is a long paragraph that will automatically wrap to multiple lines when it exceeds the maximum width. The TPDF library handles text wrapping intelligently, breaking lines at word boundaries to ensure readability."

doc.add_paragraph(long_text, 50, 200, maxWidth=500, fontSize=12, lineHeight=1.5)

# Vertically centered text
doc.vcenter('This text is centered both horizontally and vertically!', 
            fontSize=18, fontWeight='bold', color='#dc2626')

# Generate PDF
doc.compile_to_pdf('alignment_demo.pdf')
print("✅ Created alignment_demo.pdf")

