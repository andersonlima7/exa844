import urllib.request
from bs4 import BeautifulSoup

lines = []

file = open("seeds.txt", "r")

for line in file:
    line = line.strip()
    lines.append(line)
        

# print(lines[0])


print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<meta charset='UTF-8' />")
print(" <meta http-equiv='X-UA-Compatible' content='IE=edge' />")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0' />")
print("<title>Atividade 5</title>")
print("</head>")
print("<body>")


for line in lines:
    page = urllib.request.urlopen(line)
    html = str(page.read().decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')
    print("Título:", soup.title.string)
    print("<p>", soup.title.string, "</p>")
    for img in soup.find_all('img'):
        link = img.attrs.get("src")
        if(link.find('http') != -1 ):
            print("<img width='500px' src='" + link + "'/>")
        else:
            print("<img width='500px' src='" + line + "/" + link + "'/>" )




