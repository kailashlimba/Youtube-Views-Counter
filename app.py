# pip install BeautifulSoap4
from bs4 import BeautifulSoup 
import requests

searchKeyword = input("Enter a Youtube Search Keyword: " )

#Get the page with requests package 

res = requests.get('https://www.youtube.com/results?search_query='+searchKeyword)

# Get the body with LXML parser
bs = BeautifulSoap(res.text,'lxml') # pip install lxml

# Get all the elements with class yt-lockup-meta-info (the views tag class)

ViewsElements = bs.find_all('ul',class_='yt-lockup-meta-info')


totalviews = 0

for obj in ViewsElements:
	lis = obj.findChildren()
	for li in lis:
		VideoViews = li.text.replace(' views','').replace(',','')
		totalviews = totalviews + int(VideoViews)
		print(VideoViews)

print('---------------------------------')
print('Total number of Views: ' + str(totalviews))