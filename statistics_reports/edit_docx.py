import docx
import os

dictionary = {
    '#1#': 'qwe',
    '-1-': 'asd',
    '/1/': 'zxc',
}


def edit_doc(file):
    doc = docx.Document(file)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = docx.shared.Pt(14)

    for i in dictionary:
        for p in doc.paragraphs:
            if p.text.find(i) >= 0:
                p.text = p.text.replace(i, dictionary[i])
    
    return doc
