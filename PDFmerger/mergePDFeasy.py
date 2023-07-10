from pikepdf import Pdf
import sys


pdfname = "C:\\Users\\georg\\Desktop\\imma\\imma"
pdfs = []
for i in range(8):
    pdfs.append(pdfname + str(i+1) + ".pdf")

print(pdfs)

pdf = Pdf.new()
for file in pdfs:
    src = Pdf.open(file)
    pdf.pages.extend(  [src.pages[0]]   )
    
pdf.save('merged.pdf')
pdf.close()







    

    
    


    

    
