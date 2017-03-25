from bs4 import BeautifulSoup

edit = BeautifulSoup(open("unlimitedmemory.html", encoding="utf8"), "html.parser");
tags = edit.find_all("h1");
i=0
result=[]
while i<len(tags):
    a=(tags[i].text)
    result.append(a.strip())
    i=i+1

file = open("headings.html", encoding='utf-8', mode='w')
output = str(result)
file.write(output)