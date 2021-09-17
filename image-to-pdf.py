import os
from os import path
import img2pdf

folderPath = 'src'

b = ["{0}/{1}".format(folderPath, x) for x in os.listdir(folderPath) if path.splitext(x)[1] in ['.jpg', '.JPG', '.png', '.PNG', '.jpeg', '.JPEG']]
for x in b:
  with open("{0}/{1}.pdf".format(folderPath, path.splitext(path.basename(x))[0]),"wb") as f:
  	f.write(img2pdf.convert(x))