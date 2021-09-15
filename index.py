from glob import glob
from PyPDF2 import PdfFileMerger
from os import path


def get_file_name(x):
    print(path.basename(x))
    return(path.basename(x))


def pdf_merge():
    ''' Merges all the pdf files in current directory '''
    merger = PdfFileMerger()
    all_pdfs = [a for a in glob("src/*.pdf")]
    sorted_pdfs = sorted(all_pdfs, key=get_file_name)
    [merger.append(pdf) for pdf in sorted_pdfs]
    with open("output.pdf", "wb") as new_file:
        merger.write(new_file)


if __name__ == "__main__":
    pdf_merge()
    print("done")
