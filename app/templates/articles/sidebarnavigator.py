def h3_id_giver(file):
    from bs4 import BeautifulSoup
    """returns h3 headings with id from sec1 to secX where X is the number of h3 headings"""
    edit = BeautifulSoup(open(file, encoding="utf8"));
    tags = edit.find_all("h3");
    heading_count=len(tags);
    result=[];
    i=0;
    while i<(heading_count):
        a=tags[i];
        a['id']=str("sec"+str(i+1));
        result.append(a);
        i=i+1;
    file = open("workfile.html", encoding='utf-8', mode='w')
    file.write(edit.prettify(formatter="html"))
 
 
filename = input("Enter the name of the file, it needs to be in the same folder as this script: ")
    
h3_id_giver(filename)