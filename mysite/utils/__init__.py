from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

from pdfminer.converter import PDFPageAggregator,TextConverter
import io
import re ## Regular Expressions library used for python
#import tabula
#import pdfplumber

#import camelot

class Po_extract():
    def convert_pdf_to_txt(path):
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open("D:/backup_naim/po/bestseller.pdf", 'rb')
    
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp,pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
        fp.close()
        device.close()
        retstr.close()
        return (text)

    text = convert_pdf_to_txt("po.pdf")

    text=text.replace('\n','') ## Removed Newline characters

    def get_info_from_text(text,regex):
        required_info=''
        ResSearch = re.search(regex, text)
        if ResSearch:
            required_info = ResSearch.group(1)
        return required_info

    regex_Quantity ='Quantity:\s?([0-9]+)'
    regex_style_no ='No:\s\s\s\s?([0-9]+)'
    regex_order_no = '2019\s?([A-Za-z0-9]{13})'
    regex_country  = 'A/S-\s?([A-Za-z]+)'
    regex_date    = 'closing date \\(CC\\)\s?(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})'   #escape characters \\special characets\\              
    regex_color =  'variant name\s?([A-Za-z]* [A-Za-z]*)'


    Quantity_No=get_info_from_text(text,regex_Quantity)
    style_No=get_info_from_text(text,regex_style_no)
    order_No=get_info_from_text(text,regex_order_no)
    #country_Name = get_info_from_text(text,regex_country)
    #date = get_info_from_text(text,regex_date)