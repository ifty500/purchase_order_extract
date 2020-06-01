from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.conf import settings

from pathlib import Path, PureWindowsPath

from .forms import PoForm
from .models import *

from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

from pdfminer.converter import PDFPageAggregator,TextConverter
import io
import re
import os.path

import camelot
import csv

class Home(TemplateView):
    template_name = 'home.html'





def po_list(request):
    pos = Po.objects.all()
    context = {
        'pos': pos
    }
    return render(request, 'po_list.html', context)


def upload_po(request):
    if request.method == 'POST':
        pos = Po.objects.all()
        
        
        form = PoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_name = form.cleaned_data['pdf'].name
            file_name1 = form.cleaned_data['choose']
            get_file = Po.objects.last()
            print(file_name1)
            
            print(form.cleaned_data['pdf'].name)
            text=convert_pdf_to_txt(file_name)
            
            
            text=text.replace('\n','')
            #print(text)
            path = 'F:/naimProject/po_upload/media/pos/pdfs/{}'.format(file_name)
            print(path)
            
            basename = os.path.basename(path)
            print(basename)
            
            
            if file_name1 == "BestSeller":
                
                regex_Quantity ='Quantity:\s?([0-9]+)'
                regex_style_no ='No:\s\s\s\s?([0-9]+)'
                regex_order_no = 'Page\s?([A-Za-z0-9]{13})'
                regex_country  = 'S-\s?([A-Za-z]+)'
            #regex_date    = 'closing date \\(CC\\)\s?(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})'   #escape characters \\special characets\\              


                Quantity_No=get_info_from_text(text,regex_Quantity)
                style_No=get_info_from_text(text,regex_style_no)
                order_No=get_info_from_text(text,regex_order_no)
                country_name = get_info_from_text(text,regex_country)

                



                
                
            #date = get_info_from_text(text,regex_date)
            #print(date)

            elif file_name1 == "TomyHill":
                
                regex_Quantity = 'Total Units\s?([0-9\,]+)'
                regex_style_no = 'Number:\s?([0-9]+)'
                regex_order_no = ':Style\s?([A-Za-z0-9]{10})'
                regex_country = 'AP\s?([A-Za-z]{11})'

                Quantity_No = get_info_from_text(text, regex_Quantity)
                style_No = get_info_from_text(text, regex_style_no)
                order_No = get_info_from_text(text, regex_order_no)
                country_name = get_info_from_text(text, regex_country)

            elif file_name1 == "TomTailor":
                
                regex_Quantity ='PO\s?([0-9\.]+)'
                regex_style_no = 'Article-No.:\s?([0-9]+)'
                regex_order_no = 'Order-No.:\s?([0-9]+)'
                regex_country = 'S-\s?([A-Za-z]+)'

                Quantity_No = get_info_from_text(text, regex_Quantity)
                style_No = get_info_from_text(text, regex_style_no)
                order_No = get_info_from_text(text, regex_order_no)
                country_name = get_info_from_text(text, regex_country)

            elif file_name1 == "Espirit":
               
                regex_Quantity = 'Quantity\s?([0-9\.]+)'
                regex_style_no = 'Number:\s\s\s?([0-9]+)'
                regex_order_no = 'Number:\s?([0-9]+)'
                regex_country = 'S-\s?([A-Za-z]+)'

                Quantity_No = get_info_from_text(text, regex_Quantity)
                style_No = get_info_from_text(text, regex_style_no)
                order_No = get_info_from_text(text, regex_order_no)
                country_name = get_info_from_text(text, regex_country)
            

            
            
            #print(object(get_file))
            data = tables_extract(path) #need to get the full path with extension to itterate the loop
            
            print(data)
            with open(data) as f:
                reader = csv.reader(f)
                for row in reader:
                    get_file.XXS = row[1]
                    get_file.XS = row[2]
                    get_file.S = row[3]
                    get_file.M = row[4]
                    get_file.L = row[5]
                    get_file.XL = row[6]
                    get_file.XXL = row[7]
                    get_file.XXXL = row[8]
                    get_file.total = row[9]
                get_file.save()

            get_file.order = order_No
            get_file.style = style_No
            get_file.quantity = Quantity_No
            get_file.country = country_name
            #get_file.date = date
            
            
            get_file.save()
          
            return redirect('po_list')
    else:
        form = PoForm()
    return render(request, 'upload_po.html', {
        'form': form
    })



# def size_list(request):
#     pos = Po_size.objects.all()
#     context = {
#         'pos': pos
#     }
#     return render(request, 'size_list.html', context)

# def upload_size(request):
#     if request.method == 'POST':
#         po_s = Po_size.objects.all()

#         form = Po_sizeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             file_name = PoForm.cleaned_data['csv'].name
#             size = tables_extract(file_name)
#             path = 'F:/naimProject/po_upload/{}'.format(size)
            

#             with open(path) as f:
#                 reader = csv.reader(f)
#                 for row in reader:
#                     model = Po_size()
                   
#                     model.XXS=row[1]
#                     model.XS=row[2]
#                     model.S=row[3]
#                     model.M=row[4]
#                     model.L=row[5]
#                     model.XL=row[6]
#                     model.XXL=row[7]
#                     model.XXXL=row[8]
#                     model.total = row[9]
#                 model.save()
#                 return redirect('upload_size')
#     else:
#         form = Po_sizeForm()
#     return render(request, 'upload_size.html', {
#         'form': form
#     })       

         

                       







def convert_pdf_to_txt(file_name):
    print('check 1')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    filename_with_path = 'F:/naimProject/po_upload/media/pos/pdfs/{}'.format(file_name)
    fp = open(filename_with_path, 'rb')
    print('check 2')
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
    #print(text)
    return text


def get_info_from_text(text,regex):
    """
    Extract the string that matches the regular expressions
    
        1.text - text string extracted from pdf file
        2.regex - reguar expressions that is to be searched for
    returns the searched string
    """
    required_info=''
    ResSearch = re.search(regex, text)
    if ResSearch:
        required_info = ResSearch.group(1)
    return required_info






def tables_extract(file_name):
    #filename_with_path = 'F:/naimProject/po_upload/media/pos/pdfs/{}'.format(file_name)
    basename = os.path.basename(file_name)
    print(basename)
    basename_without_ex = os.path.splitext(basename)[0]
    print(basename_without_ex)
    print("hahah")

    tables = camelot.read_pdf(file_name, pages="1-end")
    table= tables[1].df
    file = table.to_csv("{}{}.csv".format('F:/naimProject/po_upload/media/pos/csv/',basename_without_ex))
    print(file)
    filename_with_path = 'F:/naimProject/po_upload/media/pos/csv/{}'.format(
        basename_without_ex.split('.')[0]+".csv")

    

    
    print(filename_with_path)
    print("code error")

    return filename_with_path
    #csv = "{}data.csv".format(settings.MEDIA_ROOT)
    

    #return table

# regex_Quantity ='Quantity:\s?([0-9]+)'
# regex_style_no ='No:\s\s\s\s?([0-9]+)'
# regex_order_no = '2019\s?([A-Za-z0-9]{13})'
# regex_country  = 'A/S-\s?([A-Za-z]+)'
# regex_date    = 'closing date \\(CC\\)\s?(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})'   #escape characters \\special characets\\              
# regex_color =  'variant name\s?([A-Za-z]* [A-Za-z]*)'

#Quantity_No=get_info_from_text(text,regex_Quantity)
#style_No=get_info_from_text(text,regex_style_no)
#order_No=get_info_from_text(text,regex_order_no)
# country_Name = get_info_from_text(text,regex_country)
# date = get_info_from_text(text,regex_date)
# color = get_info_from_text(text,regex_color)




# def po_upload_page(request):
#     return render(request, 'POUpload.html')

# def po_upload(request):
#     if request.method == "POST":
#         poFile = request.POST.get('po')
#         print(poFile)
#         po = Po(
#             pdf = poFile
#         )
#         po.save()
#         convert_pdf_to_txt(poFile)
#     return HttpResponse()

def delete_po(request, pk):
    if request.method == 'POST':
        po = Po.objects.get(pk=pk)
        po.delete()
    return redirect('po_list')
