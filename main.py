from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

read_csv = pd.read_csv("topics.csv")

for index, row in read_csv.iterrows():
    pdf.add_page()
    pdf.set_font("Times", "B", size=24)
    pdf.cell(w=30, h=12, txt=row["Topic"], align="L", ln=0 )
    pdf.line(10, 21, 200, 21)
    for i in range(row["Pages"]-1):
        pdf.add_page()


pdf.output("Output.pdf")