#Web Scraping
#Quotes from https://www.goodreads.com/quotes?page=1 page 1 to 100

class Quote:
    quote = 'Quote'
    name = 'Author'
    def __init__(self,quote,name):
    	self.quote = quote
    	self.name = name

import requests
from bs4 import BeautifulSoup
import csv

download_file = input("Enter the file name to download to (Must end with .csv) : ")
#csv = open(download_file, "w")
#csv.write('Quote,Author')
Write = csv.writer(open(download_file, 'w'))
Write.writerow(["Quote","Author"])
link = "https://www.goodreads.com/quotes?page="

for i in range(1,101):
    page = requests.get(link+str(i))
    soup = BeautifulSoup(page.content,'html.parser')
    section = soup.find(class_='quotes')
    details = section.find_all('div',class_='quoteText')
    
    for j in details:
    	convert = list(j.children)
    	extracted = Quote(convert[0],j.find('span',class_="authorOrTitle").get_text())
    	#csv.write(extracted.quote+','+extracted.name+'\n')
    	Write.writerow([extracted.quote,extracted.name])
        





