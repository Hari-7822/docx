import os
from docx import Document


doc = Document('/home/hari/Documents/python/docx/src/hello.docx')

txt = []

for i in doc.paragraphs:
    
    elem = ''
    
    for j in i.runs:
    
        if j.font.highlight_color:
           elem += j.text 
    
        if elem:
    
            txt.append(elem)
            
        

for d in txt:
    print(d)
