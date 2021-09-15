from glob import glob
from PyPDF2 import PdfFileMerger
from os import path


def first2(x):
    # src/00.pdf
    print(path.basename(x))
    return(path.basename(x))


def pdf_merge():
    ''' Merges all the pdf files in current directory '''
    merger = PdfFileMerger()
    allpdfs = [a for a in glob("src/*.pdf")]
    sortedpdfs = sorted(allpdfs, key=first2)
    [merger.append(pdf) for pdf in sortedpdfs]
    with open("output.pdf", "wb") as new_file:
        merger.write(new_file)


if __name__ == "__main__":
    pdf_merge()
    print("done")
