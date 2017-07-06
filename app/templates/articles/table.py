from bs4 import BeautifulSoup

file = str(input("Plese enter name of the file from this directory you wish to edit (example:test.html):"));
workfile = "workfile.html"
outputfile = str(input("Plese enter the desired name of output file: "));
labeltag = str(input("Need table tag? If appending to a existing table -> y/n "));
table = ""

mode = str(input("add, write:"));
   
if mode == "add":
    mode = "a";
elif mode == "write":
    mode = "w";
else:
    mode = "a";

"""creates a table for "doporučené věci" """


def createtable(table):
    table = table;
    table = "<table>"+ table;
    global filledtablestart;
    filledtablestart = table;
    
def endtable(table):
    table = table;
    table += "</table>";
    
    global filledtableend;
    filledtableend = table;

def entry(table):
    table = table;
    print("tr = row; /tr = endrow; td = column; content in each column; a = hyperlink; end = stop adding");
    value = "";
    while value != "end":
        if value == "tr":
            table += "<tr>";
                
        elif value == "/tr":
            table += "</tr>";
                
        elif value == "td":
            table += "<td>";
            content = str(input("Enter your entry:"));
            if content == "a":
                name= str(input("Enter your hyperlink name:"));
                url = str(input("Enter your url:"));
                    
                a = "<a " + "href=" + url + ">";
                table += a;
                table += name;
                table += "</a>";
                table += "</td>";
            else:
                table += content;
                table += "</td>";
        else:
            print("Invalid entry, try again.");
        print(table);
        value = str(input("Next input:")); 
    global filledtable;
    filledtable = table;

def wrap(workfile,outputfile,mode):
    """wraps the output of this script to use for the website"""
    with open(outputfile, mode, encoding="utf-8") as text_file:
        edit = BeautifulSoup(open(workfile, encoding="utf8"), "html.parser");
        text_file.write(edit.prettify(formatter="html"));
        
with open(workfile, mode) as text_file:
    entry(table);
    if labeltag == "y":
        createtable(filledtable);
        endtable(filledtablestart);
    else:
        filledtableend = filledtable
    if mode == "add":
        mode = r+b;
        text_file = open(workfile, mode)
        text_file.seek(-8,2);
    text_file.write(filledtableend);

wrap(workfile,outputfile,mode);
print(filledtableend);
input("");


    
    
    
    