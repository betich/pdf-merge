from glob import glob
from PyPDF2 import PdfFileMerger
from os import path
import re

def get_file_number(x):
    name = path.basename(x)
    res = re.findall(r'[-]?\d+', name)[0] # returns an array of all numbers in a string
    return(res)


def pdf_merge():
    ''' Merges all the pdf files in current directory '''
    merger = PdfFileMerger()
    all_pdfs = [a for a in glob("src/*.pdf")]
    sorted_pdfs = sorted(all_pdfs, key=get_file_number)
    
    for i in sorted_pdfs:
        print(i)

    [merger.append(pdf) for pdf in sorted_pdfs]
    with open("output.pdf", "wb") as new_file:
        merger.write(new_file)


if __name__ == "__main__":
    pdf_merge()
    print("done")
