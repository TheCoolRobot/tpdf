"""Basic TPDF usage example"""

from tpdf import TPDF

# Create simple document
doc = TPDF()

# Add header
doc.add_text('My First TPDF Document', 50, 50, 
             fontSize=28, fontWeight='bold', color='#1e40af')

# Add paragraph
doc.add_text('This is a simple example of using TPDF.', 50, 100,
             fontSize=14, color='#333333')

doc.add_text('You can easily add text with custom styling!', 50, 130,
             fontSize=12, color='#666666', fontStyle='italic')

# Generate PDF
doc.compile_to_pdf('basic_example.pdf')

print("✅ Created basic_example.pdf")
