# pdf merge

a script used to merge pdf files into one single output (used for collecting my classmate's files and combining them into one final document for งานสาธารณประโยชน์)

tl;dr i'm lazy

## setup

1. install python

2. install PyPDF2, img2pdf

```
pip3 install PyPDF2
pip3 install img2pdf
```

3. put all pdf files into `src`

everything is sorted numerically, so:

for front covers, name it something low like `-99.pdf`

for back covers, name it something high like: `99.pdf`

![image](https://user-images.githubusercontent.com/28398789/133363214-11461057-5546-44fa-9f92-993dc866b4fe.png)


4. run the code

for merging pdfs
```
python3 main.py
```

for converting images to pdf
```
python3 image-to-pdf.py
```

5. have fun! the output will be available as `output.pdf`
