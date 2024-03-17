import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
counter = 0
while True:
    newstring = input("Insert Title: ").replace(" ","_")
    if(newstring != ""):
        addToClipBoard(newstring)
        print(newstring + " -> in clipboard")

    else:
        print("title to short! Closing after " + str(4 - counter) + " ENTERS")
        counter += 1
    if(counter > 4):
        quit()
