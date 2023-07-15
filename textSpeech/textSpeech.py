# Program that decides when somebody has to drink.
# a button starts the gameyy
from random import choice
from time import sleep
from random import random
# to speech conversion
from gtts import gTTS
# aibility to play the converted audio
import os


# define console highlight colors..
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    MYCOL = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# stammdaten: names, drink_sortiment
names = ["Jan", "Marius", "Mary", "Elina", "Bahar","Bernd", "Deniz"]
names = ["elina", "the russian girl", "tjorven", "the X", "The drunkard","The Spaniard", "El commodore","Mr Dr. Knight","The one going to medieval stuff" ,"the nordic girl", "the economic engineer", "bernd", "Everyone older than the last person", "every german", "Bahar", "every musician", "The room owner", "Our Man in Bosch Manufacturing Solutions", "The Battery Expert", "The one recently organizing a giant Birthday Party", "The One strengthening our relations to eight floor ", "ANyone recently moving in ", " Everyone who is sitting ", "Everyone standing instead of sitting"]

drinks_prob_dict = {bcolors.OKCYAN +"water"+bcolors.ENDC : "often",
           bcolors.WARNING+"wodka"+bcolors.ENDC : "often",
             bcolors.MYCOL +"cola" + bcolors.ENDC : "often",
              bcolors.FAIL + "olive oil" + bcolors.ENDC : "seldom"}
drinks_prob_dict = {"wine" : "often", "mango shit" : "often",  "cola" : "often", "sauce hollandaise" : "seldom"}
drinks_sortiment = list(drinks_prob_dict.keys())
drinks_available = drinks_sortiment.copy() # at start time all drinks are full

def event():
    """creates a drinking event. somebody has to drink a drink that is left"""
    sleep(1)
    global drinks_available # use the global variable
    idx = drinks_available.index(choice(drinks_available)) # ychoose a drink from what is left
    if drinks_prob_dict.get(drinks_available[idx]) == "seldom":
        # maybe choose another
        if random() < 0.7:
            print("\033[91m ERR 101: drink was to ugly to be chosen. chose a new drink .. \033[ENDC")
            idx = (idx + 1) % len(drinks_available) #y choose next drink of list instead
        else:
            print("\033[91m ERR 101: ugly drink could not be prevented! .. \033[ENDC")
            pass

    drink_current = drinks_available.pop(idx) #  and remove it from availables
    chosen1 =  choice(names)
    order_formatted = bcolors.OKGREEN + chosen1 + bcolors.ENDC + " has to drink " + drink_current
    order = chosen1 + " has to drink " + drink_current
    print(order_formatted)
    t2s(order)
    print("-" * 30)
    
def countdown(max = 30, delay_sec = 0.1):
    """make a cowntdown with progress bar"""
    for i in range (max):
        print('\033[A'*2)
        progbar = "#"*i + "-" * (max-i)
        print("<{}>".format(progbar))
        sleep(delay_sec)

def timed_event(time_sec = 1):
    """drinking event with time restriction time_sec (progress bar shows the time left)"""
    event()
    print()
    countdown(max = 30, delay_sec= time_sec/30 )

def one_round(num_drinks = 3):
    """one round of num_drinks drinks. No drinks are chosen twice"""
    print("DRINKS FULL AGAIN.")
    global drinks_available
    drinks_available = drinks_sortiment.copy()
    print(drinks_available)
    for i in range(num_drinks):
        timed_event(choice([2,4,5]))
        sleep(1)


  



def t2s(mytext):
    myobj = gTTS(text=mytext, lang="en", slow=False)    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("speech.mp3")
    
    # Playing the converted file
    print("\033[91m audio output . . . \033[ENDC")
    os.system("start speech.mp3")
    sleep(5) # wait 5 sec

print("\033[95m" + "Starting up a drinking game with ranomdized drinks for randomized 4th floor members..." + "\033[ENDC")
t2s("Everyone has to go to Marius room!")
while True:
    inp = input(" Time to (re-)fill the glasses! \nType 'y' to start another round!\n\n:")
    if inp == 'y':
        one_round()

    
