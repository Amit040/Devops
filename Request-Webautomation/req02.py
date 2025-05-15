import requests
url="https://www.google.com"

responce=requests.get(url)
if responce.status_code==200:
    print(responce.status_code)
    print(responce.text[:100])
else:
    print(f"Failed to fetch the website and getting error code{responce.status_code}")