from bs4 import BeautifulSoup

html2="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Program</title>
</head>
<body>
    <h1>PW SKILLS</h1>
    <p class="info">Web Automation.</p>
    
</body>
</html>
"""
Soup=BeautifulSoup(html2,"html.parser")

print(Soup.title.text)
print(Soup.h1.text)

print(Soup.find("p",class_="info").text)
