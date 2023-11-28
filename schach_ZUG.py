# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:57:31 2018

@author: S.H.B
"""

from pylab import *
import schach_zugMOEGLICHKEITEN as zm

def zug_grafik(feld, farbe, zugarray4):
    #Bearbeitung des Arrays, damit es mit den zu verfügung stehenden Methoden verstanden wird
    zugarray4[0] = zugarray4[0] + 1
    zugarray4[1] = zugarray4[1] + 1
    zugarray4[2] = zugarray4[2] + 1
    zugarray4[3] = zugarray4[3] + 1
    
    #Prüfung des Zuges
    zugkorrekt = zugpruefung(feld, zugarray4, farbe)
    #Durchführung des Zuges
    feld = zugdurchfuehren(feld, zugarray4)
    
    
    return(feld,zugkorrekt)






def zug(feld, farbe):#(fertig) Führt einen Zug von Schwarz oder Weiß durch
    zugkorrekt = False
    
    while zugkorrekt != True:#wenn der Zug korrekt ist, wird die while Schleife nicht mehr wiederholt, wenn er falsch ist wird nach einer richtigen Eingabe gefragt
        
        #Eingabe des Zuges:
        zugarray4 = zugeingabe() #gibt Array mit 4 Zahlen von 0-8 zurück [x-Koordinate davor,y-Koordinate davor, x danach, y danach]
        
        
        #Prüfung des Zuges:
        zugkorrekt = zugpruefung(feld, zugarray4, farbe) #darf der Zug gemacht werden ? -> True, darf er nicht gemacht werden -> False
        
    #Durchführung des korrekten Zuges:
    feld = zugdurchfuehren(feld,zugarray4)
    
    return(feld)

def zugeingabe(): #(getestet) der Spieler gibt seinen Zug ein, dieser wird in einem Array gespeichert und zurückgegeben
   
    syntax = False #wird zur Überprüfung des Syntax des Zuges benutzt
    
    #Eingabe des Zuges:
    while syntax == False: #While Schleife wird beendet, wenn der Syntax stimmt
        zugarray2 = [input("Welches Feld soll angewählt werden(A1)? "),input("Zu welchem Feld soll die Figur geschoben werden(B1)? ")]
        syntax = zug_syntaxpruefung(zugarray2) #gibt True zurück, wenn der Syntax stimmt
       
    zugarray4 = zuguebersetzung(zugarray2)
    
    #Ausgabe zur Information, welcher Zug ausgeführt worden ist:
    print(str(zugarray4[0]) + str(zugarray4[1]) + "->" + str(zugarray4[2]) + str(zugarray4[3]))
    
    return zugarray4


def zugpruefung(feld, zugarray, farbe): #prüft ob der zug korrekt war und gibt dann True zurück,wenn er falsch war: False
    rueckgabe = True #Diese Variabel wird im Laufe der Funktion verändert und am Schluss zurückgegeben
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    
    za =  [zugarray[0]-1 , zugarray[1]-1 , zugarray[2]-1 , zugarray[3]-1] # nun haben alle zahlen den Wert 0-7 statt 0-8
    
    #1.Fehlermöglichkeit: Auf dem angewählten Feld befindet sich keine Figur des eigenen Teams
    
    if feld[za[0]][za[1]] == "0":
        rueckgabe = False
        print("Auf dem angewählten Feld befindet sich keine Figur")
        
    #Besitzt die angewählte Figur der Person, der diesen Zug ausführt?:
    elif farbe == "weiß" and (feld[za[0]][za[1]] in sF):
        rueckgabe = False
        print("Die angewählte Figur ist nicht ihre") 
    elif farbe == "schwarz" and (feld[za[0]][za[1]] in wF):
        rueckgabe = False
        print("Die angewählte Figur ist nicht ihre")
    else:
        #Hier Erfolgt die Prüfung, ob der gewählte Zug, nach den Schachregeln, möglich ist (sich im Array der möglichen Züge "m" befindet)
        m = zm.moeglichezuege(za[0],za[1],feld, farbe) # za[0] = y, za[1] = x ; in m werden alle möglichen Ziele der Figur auf dem Feld mit den Koordinate za[0],za[1] gespeichert
    
        #Überprüfung, ob das ausgewählte Ziel im Array m enthalten ist: zur Erinerung: Struktur von m(y1,x1,y2,x2,y3...)
        if (len(m)) > 1:
            rueckgabe = False
            for i in range(0,int(len(m)/2)):
                if m[i * 2] == za[2]: 
                    if m[i * 2 + 1] == za[3]:
                        rueckgabe = True
                        break
        else:
            rueckgabe = None
    
    return rueckgabe


def zugdurchfuehren(feld,zugarray):#(getestet) führt den Zug auf dem Feldarray durch und gibt das Feldarray wieder
    neues_feld = feld
    #Für die Übersichtlichkeit: Definierung der Indizes für den Zugriff aufs Zugarray 
    x0 = zugarray[0]-1 #Wert:0-7
    x1 = zugarray[1]-1 #Wert:0-7
    x2 = zugarray[2]-1 #Wert:0-7
    x3 = zugarray[3]-1 #Wert:0-7
    
    neues_feld[x2][x3] = feld[x0][x1]
    neues_feld[x0][x1] = "0" #das feld, von dem sich die Figur wegbewegt wird leer(also"0")

    return neues_feld


def zug_syntaxpruefung(zugarray2): #(getestet)Überprüft ob der eingegangene Zug den richtigen Syntax besitzt
    buchstaben = ["A","B","C","D","E","F","G","H","a","b","c","d","e","f","g","h"]
    zahlen = ["1","2","3","4","5","6","7","8"]
    rueckgabe = True #Diese Variabel wird im Laufe der Funktion verändert und am Schluss zurückgegeben
    
    #Längenüberprüfung:
    if len(list(zugarray2[0])) == 2 and len(list(zugarray2[1])) == 2 :
            rueckgabe = True    
    else :
        print("LängenError - Ihre Eingaben hatten nicht die gewünschte Länge. Bitte geben sie ihren Zug erneut ein")
        rueckgabe = False
    
    #Zeichenüberprüfung:
    if not((zugarray2[0])[0] in buchstaben and (zugarray2[0])[1] in zahlen and (zugarray2[1])[0] in buchstaben and (zugarray2[1])[1] in zahlen):
        rueckgabe = False
        print("ZeichenError - Ihre Eingabe war nicht in der benötigten Form. Bitte geben sie ihren Zug erneut ein")
        
    return rueckgabe

def zuguebersetzung(zugarray2):#(getestet) Übersetzt das zugarray der Form [A-H,1-8][A-H,1-8] in die Form [1-8,1-8,1-8,1-8]
    buchstabenzuordnen = np.array([[None,"a","b","c","d","e","f","g","h"],[None,"A","B","C","D","E","F","G","H"]])# wird zur Zuordnung der Buchstaben zu Zahlen benutzt
    
    #Übersetzung der Buchstabenkoordinate in eine Zahlkoordinate
    for z in range(2):#übersetzt die Buchstaben in Zahlen:
        for x in range(9):
            if (zugarray2[0])[0] == buchstabenzuordnen[z][x]:
                a = x
                print(a)
                      
    for z in range(2):
        for x in range(9):
            if (zugarray2[1])[0] == buchstabenzuordnen[z][x]:
                b = x
    #Rueckgabe des zugarray4 in der oben genannten Form:            
    return [a,int((zugarray2[0])[1]),b,int((zugarray2[1])[1])]#Variable Zug ist nun in der Form ([1,1,1,2])
