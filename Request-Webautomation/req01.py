#Pip instal request
# It is used to read the content from any url

import requests
url="https://www.google.com"
responce=requests.get(url)
print(responce.status_code) 
print(responce.text[:100]) #Print the charchter upto 100 char

