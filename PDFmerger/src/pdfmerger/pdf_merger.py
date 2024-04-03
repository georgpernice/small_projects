"""Definition of PDFMerger class for merging pdfs and handling of drag and drop start of this package hopefully soon."""
from pikepdf import Pdf
import sys
import os
from pathlib import Path
class PDFMerger:
    def __init__(self, dest_path : Path) -> None:
        self.destination_path = dest_path
    def merge(self, pdfs : list[Path]):
        """Merge a list of documents into one called merged.pdf."""
        pdf = Pdf.new()
        for file in pdfs:
            src = Pdf.open(file).pages
            pdf.pages.extend(src) 
        Path.mkdir(self.destination_path.parent, parents=True, exist_ok=True) 
        pdf.save(self.destination_path)
        return self.destination_path

# try: #appending wanted -> append file
#     droppedFile = sys.argv[1]
#     try:        
#         statefile = open("state.txt", "r")
#         statefile.close()
#         statefile = open("state.txt", "a")
#         statefile.write(droppedFile+"\n") # ACHTUNG Enter am File-Ende
#         statefile.close()
#         print("appended")
#     except:# deleted statefile
#         print("Restart without file!")
        
# except:# ending or restart wanted
#     print("No File given.")
#     try:# restart -> recreate statefile
#         statefile =  open('state.txt','x')
#         statefile.close()
#         print("appending. next time open with file!")

#     except:# ending -> merge everything from statefile delete afterwards
#         statefile =  open('state.txt','r')
#         pdfs = statefile.readlines()
#         statefile.close()
#         os.remove("state.txt")
        
#         pdf = Pdf.new()
#         for file in pdfs:
#             pdf.pages.extend(  [Pdf.open(file).pages[0]]   )
            
#         pdf.save('merged2.pdf')
#         pdf.close()
#         print("merged. next time open without file for restart!")
        




    
    

    
    


    

    
