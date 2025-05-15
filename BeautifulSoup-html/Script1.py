#BeautifulSoup is used for fetching data from html
#import BeautifulSoup --> pip install beautifulsoup4

from bs4 import BeautifulSoup

html='<html><body><h1>Welcome to PW SKILLS</h1></body></html>'

# create an object
soup=BeautifulSoup(html,"html.parser")
print(soup.h1.text)

