import os
from docx import Document


file = '/home/hari/Documents/python/docx/src/hello.docx'
doc = Document(file)

txt = []

for i in doc.paragraphs:
    
    elem = ''
    
    for j in i.runs:
    
        if j.font.highlight_color:
           elem += j.text 
    
        if elem:
    
            txt.append(elem)


file2 = open('/home/hari/Documents/python/docx/txt/hello.txt', 'w')
            
for d in txt:
    file2.write(d+'\n')
