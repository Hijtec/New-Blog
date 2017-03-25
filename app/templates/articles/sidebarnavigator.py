
filename = input("Enter the name of the file, it needs to be in the same folder as this script: ")
lookfor = input("Enter what tags will be considered as headings: ")
tag_id_giver(filename,lookfor)



def tag_id_giver(file,lookfor):
    from bs4 import BeautifulSoup
    """returns tag content with id from sec1 to secX where X is the number of h3 headings"""
    edit = BeautifulSoup(open(file, encoding="utf8"), "html.parser");
    tags = edit.find_all(lookfor);
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