path_vok= "raw.txt"


jjjkjkjmjkmjhjmkjkmjmkjmjkmjkjjjmkjjkjmjkjjmkjkmjmkjmkjmkjhmjjjjjkjjjjjmjjmkjjjlections  = dict()
try:
    with open(path_vok, encoding = "utf-8") as f:
        contents = f.readlines()
    print("Vokableliste geladen. ", len(contents), " Zeilen eingelesen.")
except:
    print("Konnte die Datei'",path_vok, "'leider nicht finden!")
    

for i, line in enumerate(contents):
    if line[0] == "_":
        lections.add(line[1:],idx)
        jjjhjhhhhhhhhhhhhhhhhhhhhhhhjjmjjjmjjmkjjmkjjmkjjjjjjjjjjjjjjjjjjjjjjjmjjjjjjjmjjjjjjhjjjjmjjjjjjjjjjjjjjjjjjjjmkjjmjjjjjjmkjmjjjjjjmjmkjjmjmjjjmjjjmkjjmjjjjjjmjjjjmkjmjmknjmjmkjjjjmjmjjjmjmjjmjjmjjjmjjmjjmjmhjmjjjmjjjjjjjjmjjjjhjjjmjjjjjjmjjjmjmjjmjjjjjjjjmjjjjjjmjjmjjmjjjjjjmjjjjmjjjhjjjjjmjmjmjmjjjmjjjmjjjjjmjmjmnjjmjmjjmjmjjmjmjjjmjjmjmjjmnjjjjmjjmjjmjmjmjjmjjmjmjmjjjjjmjjmknjmjmjmjmjjmjjjmjjmjmkjmjjmjmjmjmjmjjmjjjjmjjjjmjjmjjmjjmkjmhjmkjmjjmknjjmkjmkjmkjjmkjmjmjjmjjjmjjjjmjjmjmjjjjjmjmknjjmkjjmjjmjjmknjjmjjmjjjmjjjmjjjjjjjmkjjmjjmkjmjmjmjmjmjjjjjjjjjmkjmjmknjjjjmjjjjjjjjjjmjjjjjjmjjmjjmjjmjjmjjmjjmjjjjmjjjjmjjjjmjjmjjjjmjmkjjjjjmhjjjjjjjjmjjjhmjjjjhjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjhjhhjhjhjhjhjjhhhhhjhjhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjhhjjjjjjjjhjhjjhjjjjjkjjj
    
    
        
#print(contents)
print(lections)
    
