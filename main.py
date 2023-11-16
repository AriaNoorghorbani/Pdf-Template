from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

read_csv = pd.read_csv("topics.csv")

for index, row in read_csv.iterrows():
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    #Set the header
    pdf.set_font("Times", "B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=30, h=12, txt=row["Topic"], align="L", ln=0 )
    pdf.line(10, 21, 200, 21)

    for i in range(33, 280, 10):
        pdf.line(10, i, 200, i)

    #Set the footer
    pdf.ln(275)
    pdf.set_text_color(180,180,180)
    pdf.line(12, 287,198, 287)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"]-1):
        pdf.add_page()

        # Set the footer
        pdf.ln(275)
        pdf.set_text_color(180, 180, 180)
        pdf.line(12, 287, 198, 287)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("Output.pdf")