import PyPDF2
import sys
import os

path = "./pdfs"

merger = PyPDF2.PdfMerger()
pdf = "no"

while pdf == "no" : 
 fileName = input("What should be the name of the combined pdf? (with .pdf): ")

 if not fileName.endswith('.pdf'):
    print("The file name must end with .pdf")
    pdf = "no"
 else:
     pdf = "yes"
    

print(r"Do the pdfs that you want to merge in this folder: C:\Users\noeba\Desktop\python\pdfs")
input("Is it done? (y/n): ")

for file in os.listdir(path):
    if file.endswith(".pdf"):
     print(f"merging{file}...")
     full_path = os.path.join(path, file)
     merger.append(full_path)

merger.write(fileName)