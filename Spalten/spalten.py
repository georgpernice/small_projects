from time import sleep
SPALTEN_headings = {'S': "Situationsanalyse",
           'P' : "Problemeingrenzung",
           'A':"Alternative Lösungen",
           'L': "Lösungsauswahl",
           'T':"Tragweitenanalyse",
           'E':"Entscheiden & Umsetzen",
           'N':"Nachbereiten & Lernen"}
SPALTEN_summary = {key:val for (key,val) in zip(SPALTEN_headings.keys(), [
    [ "Situation erkennen und verstehen", "Zielrichtung und Vorgehensweise des weiteren PLP bestimmen", "Informationsbasis für die Lösungssuche schaffen"],
    [ "Identifikation des eigentlichen Problems","\t bewusste Klärung des Ist- bzw Soll-Zustandes", "genaue Ermittlung der Gründe für die Abweichung", "Aufstellung und Untersuchung der Kausalkette"],
    ["möglichst viele alternative Lösungsmöglichkeiten zur Beseitigung einer Abweichung erzeugen", "bewusste Lösungsvielfalt um Wahrscheinlichkeit zu erhöhen, tatsächlich beste Lösung zu finden", "Entscheidungsgrundlage für Lösungsauswahl bilden"],
    [ "Aus vorhandenen Lösungsvorschlägen die technisch und wirtschaftlich optimale Lösung auswählen"],
    ["Erfassung potentieller Einflüsse, die eine erfolgreiche Umsetzung der Problemlösung und der Erreichung des Solls gefährden", "Ursachen für die Risiken ermitteln", "Maßnahmen gegen Ursachen erarbeiten", "schadensbegrenzende Maßnahmen erarbeiten"],
    [ "Herausforderung für Projektmanagement", "Komplexität der Inhalte und Problemstellungen", "multidisziplinäre Problemstellungen", "Anforderungen bzgl. Zeit, Kosten, Qualität", "Beteiligung von vielen Menschen"],
    [ " nicht angeg."],
    ])
    }

SPALTEN = {key:val for (key,val) in zip(SPALTEN_headings.keys(), [
    ["Situation erfassen und sichten" , "Situation aufklären", "Situationsnachbehandlung festlegen"],
    ["Abweichungen erkennen", "Abweichungen beschreiben und abgrenzen", "mögliche Ursachen für Abweichungen erkennen", "Ursachen nach Wahrscheinlichkeit bewerten"],
    ["Lösungsraum abstecken", "Lösungsvorschläge generieren", "Lösungsvorschläge analysieren und konkretisieren", "Lösungsvorschläge beschreiben und speichern"],
    ["Entscheidungsthema formulieren", "Entscheidungsthema hinterfragen", "Informationscheck", "Lösungsauswahl (oder evtl. Entscheidungsthema neu formulieren)"],
    ["7 Schritte für Chancen:" ,"Projektwegbeschreibung klären (Hauptaufgabe, Teilvorgänge, RB)", "kritische Schritte ermitteln und bewerten", "potentielle CHANCEN ermitteln und bewerten", "Ursachen für CHANCEN ermitteln und bewerten",
     "fördernde Maßnahmen planen", "verwertende Maßnahmen festlegen", " Maßnahmen in das Projekt einbinden ", " #### 7 Schritte für Risiken",
     "Projektwegbeschreibung klären (Hauptaufgabe, Teilvorgänge, RB)", "kritische Schritte ermitteln und bewerten",
     "potentielle  RISIKEN ermitteln und bewerten", "Ursachen für RISIKEN ermitteln und bewerten",
     " Vorbeugung durch Gegenmaßnahmen und einbinden in Projektweg", "Vorsorge durch Erarbeiten von schadensbegrenzenden Maßnahmen",
     "Restrisiko prüfen! Akzeptabel? Wenn nicht WDH!"],
    ["kein fester Ablauf für Entscheiden und Umsetzen"],
    ["kein fester Ablauf für Nachbereiten und lernen"]]
                                                 )}

def formatSL(stringlist, mode = "num"):
    """ format the string list in bullet points or numbered list"""
    if mode == "num":
        formatted = [str(num)+". \t"+element for num, element in enumerate(stringlist)]
    else:
        formatted  = ["\u2022"+element for num, element in enumerate(stringlist)]

    return formatted

def printFormattedQuizzy(strList, timeintervall = 3):
    """ print quizzy as bullet points or numbered list """
    strList = formatSL(strList, mode = "notnum")
    for i in strList:
        input()#sleep(timeintervall)        
        print(i)
        
def pfq(letter, dictionary, intervall = 4):
    printFormattedQuizzy(dictionary.get(letter), intervall)
    #sleep(PAUSE)
    #print("\n"*20)


PAUSE = 7
for k in SPALTEN.keys():
    ####
    #k = "P"
    ####
    dictionary = SPALTEN_summary
    if dictionary == SPALTEN_summary:
        heading = "Zusammenfassung"
    else:
        heading = "Schritte"
    print(10*"-"+k+" ("+SPALTEN_headings.get(k)+") "+heading)
    pfq(k, dictionary)
    

