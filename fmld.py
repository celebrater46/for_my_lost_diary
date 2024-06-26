import docx

def say_hello():
    print("Hello world!!!!!!!!!")

say_hello()

def create_txt(doc):
    f = open("files/converted.txt", "w", encoding='utf-8')
    for paragraph in doc.paragraphs:
        f.write(paragraph.text + "\n")
    f.close()

def open_docx():
    document = docx.Document("files/test.docx")
    create_txt(document)

open_docx()