from bs4 import BeautifulSoup
import re
edit = BeautifulSoup(open("APH.html", encoding="utf8"))
tag = edit.find_all("h3")
lentag = len(tag)
i=range(20)
print(i)
print(lentag)
