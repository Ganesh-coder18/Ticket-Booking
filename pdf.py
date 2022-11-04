from fpdf import FPDF
pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial",size=16)

f = open("3.txt","r")

for x in f:
    pdf.cell(250,10,txt=x,ln=1,align="B")

pdf.output("1.pdf")

print("done")