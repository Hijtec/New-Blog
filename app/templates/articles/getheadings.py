from bs4 import BeautifulSoup

edit = BeautifulSoup(open("APH.html", encoding="utf8"));
tags = edit.find_all("h3");
i=0
result=[]
while i<len(tags):
    a=(tags[i].text)
    result.append(a.strip())
    i=i+1

file = open("headings.html", encoding='utf-8', mode='w')
output = str(result)
file.write(output)