import os
from docx import Document

base = os.path.abspath('/home/hari/Documents/python/docx/')

file = os.path.join(base, 'src/hello.docx')
doc = Document(file)

txt = []

for i in doc.paragraphs:
    
    elem = ''
    
    for j in i.runs:
    
        if j.font.highlight_color:
           elem += j.text 
    
        if elem:
    
            txt.append(elem)


file2 = open(os.path.join(base, 'txt/hello.txt'), 'w')
            
for d in txt:
    file2.write(d+'\n')
