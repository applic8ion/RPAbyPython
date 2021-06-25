
import pdfplumber

def get_text_from_pdf(filepath, page_from, page_to):
    with pdfplumber.open(filepath) as pdf:
        total_pages = len(pdf.pages)
        if total_pages < int(page_to):
            page_to = total_pages
        
        text_list = []
        for page in range(int(page_from) - 1, int(page_to)):
            print('page: ', page + 1)
            pdfObj = pdf.pages[page]
            text = pdfObj.extract_text()            
            text_list.append(text)
        # print(text_list)
        return text_list

# from io import StringIO
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser

# def get_text_from_pdf(filepath, page_from, page_to):
#     output_string = StringIO()
#     with open(filepath, 'rb') as pdf:
#         parser = PDFParser(pdf)
#         doc = PDFDocument(parser)
#         rsrcmgr = PDFResourceManager()
#         device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#         interpreter = PDFPageInterpreter(rsrcmgr, device)
#         for pageNum, page in enumerate(PDFPage.create_pages(doc)):
#         # for pageNumber, page in enumerate(PDFPage.get_pages(pdf)):
#             print('pageNum: ', pageNum)
#             if page_from - 1 <= pageNum and pageNum < page_to:
#                 interpreter.process_page(page)
#     print(output_string.getvalue())


# from PyPDF2 import PdfFileReader
# def get_text_from_pdf(filepath, page_from, page_to):
#     pdf = PdfFileReader(open(filepath, 'rb'))
#     total_page = pdf.numPages
#     # 종료 페이지가 전체 페이지보다 크면 전체페이지로 추출
#     if total_page < int(page_to):
#         page_to = total_page
#     for page in range(int(page_from) - 1, int(page_to)):
#         pageObj = pdf.getPage(page)
#         return pageObj.extractText()
#         # return pageObj.extractText().splitlines()
#         # print("text: {}".format(text))
#         # for line in text:
#         #     sentence = ''.join(line.replace('\n', ''))            
#         #     print(sentence)