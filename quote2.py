import requests
from bs4 import BeautifulSoup
import csv

link = "http://quotes.toscrape.com/page/"
filename = input('Enter csv file name to download to : ')
out = csv.writer(open(filename, 'w'))
out.writerow(["Quote","Author"])

i = 1
while 1:
	page = requests.get(link+str(i)+'/')
	if page.status_code!=200:
	    break
	soup = BeautifulSoup(page.content,'html.parser')
	nextbutton = soup.find('li',class_ = 'next')
	if nextbutton==None:
		break
	quotes = soup.find_all('span',class_ = 'text')
	authors = soup.find_all('small',class_='author')
	for j,k in zip(quotes,authors):
		out.writerow([j.get_text(),k.get_text()])
	i = i+1