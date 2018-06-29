# def makerawtext():
	

# def cleanrawtext():


# def returnparsed():

# import pypdf2
# from pdfminer.pdfpage import PDFpage

import PyPDF2

import docx

import string

import logging

logging.basicConfig(level=logging.DEBUG)

def fetch_pdf_page(file_name):

  # try:

    links = []

    file_pointer = open(file_name,'rb')



    # Setting up pdf document

    pdf_pages =PyPDF2.PdfFileReader(file_pointer)
    print(type(pdf_pages))

    num_pages=pdf_pages.getNumPages()
    #fetches URLs

    for pageno in range(0,num_pages):
      page=pdf_pages.getPage(pageno)
      page_data=page.extractText()
      print(type(page_data))
      print(page_data)

      # if 'Annots' in page.attrs.keys():

      #   link_object_list = page.attrs['Annots']

        # Due to implementation of pdfminer the link_object_list can either

        # be the list directly or a PDF Object reference

    #     if type(link_object_list) is not list:

    #       link_object_list = link_object_list.resolve()

    #     for link_object in link_object_list:

    #       if type(link_object) is not dict:

    #         link_object = link_object.resolve()

    #       if link_object['A']['URI']:

    #         links.append(link_object['A']['URI'])

    # file_pointer.close()

    # return links
  # except (Exception, exception_instance):

  #   logging.error('Error while fetching URLs : '+str(exception_instance))

    return ''
#Extract text from PDF


def getPDFContent(path):

    content = ""

    # Load PDF into pyPDF

    pdf = PyPDF2.PdfFileReader(open(path, "rb"))

    # Iterate pages

    for i in range(0, pdf.getNumPages()):

        # Extract text from page and add to content

        content += pdf.getPage(i).extractText() + "\n"

    # Collapse whitespace

    content = " ".join(content.replace(u"\xa0", " ").strip().split())

    return content



#Extract text from DOCX

def getText(filename):

    doc = docx.Document(filename)

    fullText = ""

    for para in doc.paragraphs:

        fullText += para.text

    return fullText



#To store extracted resumes

resume = ""

#Select a path to the file - code needs os.path #to be addded

filename = input("Enter file name / path : ")

#Invoking document parsers based on file format

#Note: for TXT - do a normal f.read()

if filename.endswith(".pdf"):

    resume = getPDFContent(filename).encode("ascii", "ignore") 
    print(type(resume))

elif filename.endswith(".docx"):

     resume = getText(filename).encode("ascii", "ignore")
     print(type(resume))  

else:

    print("File format is currently not supported")

    exit(0)



print("processing..... \nplease wait....")

#Importing NLTK for stopword removal and tokenizing

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords



#Tokenizing/ Filtering the resume off stopwords and punctuations 

print("tokenizing the given file ......")

tokens = word_tokenize(resume.decode("utf-8"))

punctuations = ['(',')',';',':','[',']',',']

stop_words = stopwords.words('english')

#storing the cleaned resume

filtered = [w for w in tokens if not w in stop_words and  not w in string.punctuation]

print("removing the stop words....\nCleaning the resumes....\nExtracting Text .......")

# print(filtered)

#get the name from the resume

name  = str(filtered[0])+' ' +str(filtered[1])

print("Name : " + name)



#using regular expressions we extract phone numbers and mail ids

import re

#get contact info - from resume

#email

email = ""

match_mail = re.search(r'[\w\.-]+@[\w\.-]+', resume.decode("utf-8"))

#handling the cases when mobile number is not given

if(match_mail != None):

    email = match_mail.group(0)

print("Email : " + email)



#mobile number

mobile = []

match_mobile = re.search(r'((?:\(?\+91\)?)?\d{9})',resume.decode("utf-8"))
if(match_mobile):
	mobile.append(match_mobile.group(0))

match_mobile_2 = re.search(r'(?:\w{3}-\w{3}-\w{4})',resume.decode("utf-8"))	
if(match_mobile_2):
	mobile.append(match_mobile_2.group(0))

match_mobile_3 = re.search(r'(?:\(\w{3}\)\w{3}-\w{4})',resume.decode("utf-8"))	
if(match_mobile_3):
	mobile.append(match_mobile_3.group(0))

#handling the cases when mobile number is not given

if(mobile != None):
	print("Mobile : ")
	# print('[%s]' % ', '.join(map(str, mobile)))
	for item in range(len(mobile)):
		print(mobile[item])
	#print the url list

else:
	print("Mobile : " + " ")

url=[]
# if(fetch_pdf_urls(filename)!=None):
# 	url= fetch_pdf_urls(filename)
# print("URL : " + url)

# match_url = re.search(r'((?:/((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/)',resume.decode("utf-8"))
match_url = re.search(r'((?:/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/)/)',resume.decode("utf-8"))
if(match_url):
	url.append(match_url.group(0))

# match_url = re.search(r'(?:\w{3}-\w{3}-\w{4})',resume.decode("utf-8"))	


# if(match_url == None):
# 	match_url = re.search(r'(?:\(\w{3}\)\w{3}-\w{4})',resume.decode("utf-8"))	

#handling the cases when mobile number is not given

if(url != None):
	print("URLs : ")
	for item in range(len(url)):
		print(url[item])
	#print the url list

else:
	print("URLs : " + " ")



parsed_resume = ' '.join(filtered)

# print("Parsed Resume in plain Text : ", parsed_resume)

r = str(parsed_resume)

