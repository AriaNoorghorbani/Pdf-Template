from fpdf import FPDF

pdf = FPDF(orientation="L", unit="mm", format="A4")

pdf.add_page()

pdf.set_font("Times", "B", size=12)

pdf.cell(w=30, h=12, txt="Hello There", border=1, align="L", ln=0 )
pdf.cell(w=0, h=12, txt="Hello There", border=1, align="L", ln=1 )


pdf.output("Output.pdf")