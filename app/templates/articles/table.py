from bs4 import BeautifulSoup

file = str(input("Plese enter name of the file from this directory you wish to edit (example:test.html):"));
outputfile = str(input("Plese enter the desired name of output file: "));
mode = str(input("add/append, write/new:"));





def createtable():
    
    
    
    
    
humaninput(mode)
def humaninput(mode):
    if mode == "add" OR "append":
        global mode = "a"
    elif mode == "write" OR "new":
        global mode = "w"
    else:
        global mode = "a"



def wrap(file,outputfile,mode):
    """wraps the output of this script to use for the website"""
    with open(outputfile, mode, encoding="utf-8") as text_file:
        edit = BeautifulSoup(open(file, encoding="utf8"), "html.parser");
        text_file.write(edit.prettify(formatter="html"))