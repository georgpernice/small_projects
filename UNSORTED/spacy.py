import time as t
def spacy (inp):
    name = inp#input("Titel eingeben: ")
    res=""
    for i in name:
        
        if(i  != " "):
            res = res + i
        else:
            res = res + "_"
    return (res+"\n")

def spacyTimo(inp):
    return (inp.replace(" ","_"))

while True:
    print(spacy(input("Titel:")))
