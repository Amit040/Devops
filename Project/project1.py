#Create a project to fetch the data from URL and extract the link and img from that

import requests
from bs4 import BeautifulSoup

url="https://www.google.com"  #Fetching data from here
Responce=requests.get(url)
soup=BeautifulSoup(Responce.text,"html.parser")

# Extract and print the page title
print(soup.title.text)
print(Responce.status_code)

# Extract and print the link
print("\n Links:")
for link in soup.find_all("a"):
    print(link.get("href"))   #href is used to find the link which open by single click

## Extract and print the image
print("\n Image")
for img in soup.find_all("img"):
    print(img.get("src"))