
from PyPDF2 import PdfFileReader, PdfFileWriter
import pdfplumber


def split(path, name_of_split):
    pdf = PdfFileReader(path)
    pdf1 = pdfplumber.open(path)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        page1 = pdf1.pages[page]
        text = page1.extract_text()
        name_of_split = text.split('\n',1)[0]

        if (name_of_split.__contains__(".")):
            output = f'{name_of_split}pdf'
        else:
            output = f'{name_of_split}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
    path = r'pathofdownloadedfile'
    split(path, 'name')
