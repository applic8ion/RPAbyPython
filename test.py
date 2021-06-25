import re
from tkinter.filedialog import test

re_page_number = re.compile(r'([0-9]+ - [0-9]+)')    # 페이지 번호 여부 확인
re_section = re.compile(r'([0-9]+ \w+)')    # 장절 여부 확인
re_section_number = re.compile(r'(([0-9+]+)(\.[0-9]+)?[^\.])')  # 장절 번호 추출

def test1():
    line_strip = """2 Interoperability Concepts
    12.2 sfdaf
    2.1 Overview
    12.34 asdfadsfaf
    1. A UAS can be divided into five distinct elements as shown in Figure 3 - 1. The UA element consists of the airframe, propulsion and the avionics required for UA and flight management. The payload element is comprised of payload packages. These can be sensor systems and associated recording devices that are installed on the UA, or they can consist of stores (e.g., weapon systems, and associated control/feedback mechanisms, or both). As illustrated, the data link element consists of the Vehicle Data Terminal (VDT) in the UA and the Control Data Terminal (CDT) which may be located on the surface, sub-surface or air platforms. Control of the UAS is achieved through the UCS and data link elements. Although shown as part of the UAS surface component, the UCS"""
    try:    
        m2 = re_section_number.match(line_strip)
        if m2:
            print('Match found: ', m2.group())
    except:
        pass


class TextFromPdf:
    def __init__(self):
        self.text_from_pdf = ''
    
    def get(self):
        print(self.text_from_pdf)
        return self.text_from_pdf

def test2():
    text_from_pdf = TextFromPdf()
    text_from_pdf.text_from_pdf = '123'
    text_from_pdf.get()

test2()