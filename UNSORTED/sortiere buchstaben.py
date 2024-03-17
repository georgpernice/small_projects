lexikon = open("deutschewoerter.txt", "r")
chaostext = open ("chaostext.txt", "r")
deutschwoerter = lexikon.read().split("\n")
chaoswoerter = chaostext.read().split(" ")

def compare(w1,w2):
    w1 = w1.lower()
    w2 = w2.lower()
    if len(w1) != len(w2):
        return False
    for b in w1:
        if w2.find(b)==-1:
            return False
    for b in w2:
        if w1.find(b)==-1:
            return False
    loesung=""
    for b2 in w2: #für alle sortierten buchstaben i
        added = False
        for b1 in w1:#für alle noch nicht addierten buchstaben b1
            if (b2==b1 ):#gehe  die buchstaben des chaosworts durch und vergleiche mit buchstabe i
                if(added == False):
                    loesung = loesung + b1
                    added = True
    if loesung != w2:
        
        print(w2)
        print(w1)
        return False
        
            
    return True
line=""
for chaoswort in chaoswoerter:
    for deutschwort in deutschwoerter:
        if(compare(chaoswort,deutschwort)) == True:
            line = line + " " + deutschwort.lower()
        else:
            line = line + "(" +chaoswort +")"
    print(line)
        
    
                    
                        
print(compare("Wiederherstellung","Wiederherstellung"))
