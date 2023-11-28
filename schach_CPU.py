# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:35:22 2018

@author: S.H.B
"""

from pylab import *
import random as rn
import schach_zugMOEGLICHKEITEN as zm
import copy

sF = ["T","S","L","D","K","B"]
wF = ["t","s","l","d","k","b"]
aF = sF + wF


def cpu_main(feld,farbe,schwierigkeit):#(getestet) gibt ein feld Array zurück, bei dem der Computergegner einen Zug gemacht hat
    amz_array = alle_moeglichen_zuege(feld,farbe,schwierigkeit)# amz_array in Form: yeigen1,xeigen1,yziel1,xziel1,typeigen1,typziel1,bewertung1...
    #print(amz_array)
    #greift auf Bewertungen der züge zu und fasst sie im Array b zusammen(getestet)
    b = []
    for i in range (0,int((len(amz_array))/7)):
        b.append(amz_array[i * 7 + 6])
    #print("b:",b)
    #erzeugt ein array index_maxb, in dem die Indizes der Elemente gespeichert werden, wenn diese max(b) groß sind
    index_maxb = []
    for j in range(0,len(b)):
        if b[j] == max(b):
            index_maxb.append(j)
    #print("max:", index_maxb)
    #ermittelt zufälligerweise einen Index, welcher im array index_maxb benutzt wird
    i = rn.randint(0,len(index_maxb)-1) 
    #print(i)
    
    #findet nun die y und x-Werte aus dem amz_array herraus, die zum Index in index_maxb passen
    print(amz_array)
    ya = amz_array[index_maxb[i] * 7]
    xa = amz_array[index_maxb[i] * 7 + 1]
    ye = amz_array[index_maxb[i] * 7 + 2]
    xe = amz_array[index_maxb[i] * 7 + 3]
    
    #Führt den Zug durch und ändert die Werte der einzelnen Felder
    feld[ye][xe] = feld[ya][xa]
    feld[ya][xa] = "0"

        
    return(feld)
        
        
        
        
#wichtige Funktionen:
    
def alle_moeglichen_zuege(feld,farbe,schwierigkeit): #amz_array in Form: yeigen1,xeigen1,yziel1,xziel1,typeigen1,typziel1,bewertung1...
    aef, aeft = alle_eigenen_figuren(feld,farbe)
    amz_array = []
    
    for i in range(0,int(len(aef) / 2)): #geht jede einzelne eigene Figur durch und erzeugt ein Array mit den möglichen Zügen
        mz = zm.moeglichezuege(aef[i * 2], aef[i * 2 + 1], feld, farbe)
        for j in range(0,int(len(mz)/2)):#geht jede Zugmöglichkeit einer Figur durch und lässt sie bewerten
            zb = zug_bewertung_main(aef[i * 2], aef[i * 2 + 1], mz[j * 2], mz[j * 2 + 1], feld, schwierigkeit)
            
            amz_array = amz_array + zb#Informationen werden nun nacheinander an das anz_array angeheftet
    
    return (amz_array)#zur Erinnerung:  7. stelle im Array (beginn bei 0 .. also 6)
            
        
def zug_bewertung_main(ya,xa,ye,xe,feld,schwierigkeit): #Gibt ein geordnetes Array für jeden Zug zurück; jedem Zug wird eine Bewertung zugeordnet; Form:yeigen,xeigen,yziel,xziel,typeigen,typziel,bewertung
    #Bewerten jeden Zug mit 0; -> jeder Zug ist dadurch gleichgewertet
    if schwierigkeit == "leicht":#(fertig)
        bewertung = 0
        zb = [ya,xa,ye,xe,feld[ya][xa],feld[ye][xe],bewertung]#alle Züge sind mit 1 gleich bewertet
    
    #hier bewertet ein Allgorithmus jeden Zug mit einer anderen Wertung; in der cpu_main() wird dann der am besten bewertete Zug ausgeführt
    if schwierigkeit == "normal":
        bewertung = zug_bewertung_entscheider(ya,xa,ye,xe,feld)

        zb = [ya,xa,ye,xe,feld[ya][xa],feld[ye][xe],bewertung]
        
    if schwierigkeit == "schwer":#noch nicht fertig
        bewertung = 0
        zb = [ya,xa,ye,xe,feld[ya][xa],feld[ye][xe],bewertung]
        
    return (zb)



def zug_bewertung_entscheider(ya,xa,ye,xe,feld):#gibt die Bewertung für einen Zug im normalen Spielmodus zurück
    bewertung = 0
    figur_typ = feld[ya][xa] #Typ der eigenen Figur 
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    #Dictionary mit den Bewertungen der Figuren 
    wertung_figur = {"b" : 2 ,"B" : 2 ,"k" : 3 ,"K" : 3 ,"s" : 4 ,"S" : 4 ,"l" : 4 ,"L" : 4 ,"t" : 5 ,"T" : 5 ,"d" : 7 , "D" : 7}

    
    
    #gegner Figuren werden festgelegt/ eigene Farbe wird festgestellt
    if feld[ya][xa] in sF:
        gF = wF #gF = gegnerFiguren
        vF = sF #vF = verbündeteFiguren
        eigene_farbe = "schwarz"
        gegner_farbe = "weiß"
    elif feld[ya][xa] in wF:
        gF = sF
        vF = wF
        eigene_farbe = "weiß"
        gegner_farbe = "schwarz"
    #Fehlermeldung, falls die Figur nicht erkannt wird
    else:
        print(feld[ya][xa])
        raise NameError("Error - Schwerwiegender Fehler in zug_bewertung_entscheider - Figur nicht erkannt")
    
    
   #Bewertung aufgrund eines Gegners, der geschlagen werden kann (wichtig gegner Figur und Deckung der anderen Figur -> Vergleich mit eigener Wertung )
    if feld[ye][xe] in gF:
        bewertung = bewertung + 1 #bewertet den Zug automatisch höher
        bewertung = bewertung + wertung_figur[feld[ye][xe]] #bewertet den Zug relativ zur geschlagenen Person höher
        

        
        
   #Verringerung der Bewertung des Zuges, wenn die Figur auf ein Feld zieht, welches vom Gegner im Visier ist    
    #Lädt sich Informationen über die Art der Deckung der gegnerischen Figuren in die 3 folgenden Variabeln
    gegner_status_deckung, gegner_vielfachheit_deckung, gegner_art_deckung = feld_gedeckt(ya,xa,ye,xe,feld,gegner_farbe)
        #Abziehen von Bewertungs-Punkten für den Zug, wenn das Ziel gut gedeckt ist
    if gegner_status_deckung == True:
        bewertung = bewertung - 1
            
        
  #Erhöhung der Bewertung des Zuges, wenn die Figur auf ein Feld zieht, welche von Verbündeten im Visier ist
    eigene_status_deckung, eigene_vielfachheit_deckung, eigene_art_deckung = feld_gedeckt(ya,xa,ye,xe,feld,eigene_farbe)
    if eigene_status_deckung == True:
        bewertung = bewertung + 1
    
    #Vergleicht die Deckungen des Zielfelds (Ist die Deckung des Gegners oder die durch eigene Figuren besser?):
        
    #für den Fall, dass die Deckung der gegner Figuren besser ist:
    #erstellt Variabel für die Abbruchbedingung der folgenden while Schleife
    evd_schleife = copy.deepcopy(eigene_vielfachheit_deckung)
    #Zieht Wertungspunkte ab, je größer die gegner Deckung im Vergleich zur eigenen ist; desto mehr Wertungspunkte
    while gegner_vielfachheit_deckung > evd_schleife:
        bewertung = bewertung - 1
        evd_schleife = evd_schleife + 1
        #!!! weiter mit Bezug auf den Wert der Figuren, die an der Deckung beteiligt sind
    
    
    #das selbe für den Fall, dass die Deckung der eigenen Figuren besser ist
    gvd_schleife = copy.deepcopy(gegner_vielfachheit_deckung)
    #Fügt Wertungspunkte hinzu, je größer die eigene Deckung im Vergleich zur gegner Deckung ist; desto mehr Wertungspunkte
    while eigene_vielfachheit_deckung > gvd_schleife:
        bewertung = bewertung + 1
        gvd_schleife = gvd_schleife + 1
            
    
   #Erhöhung der Bewertung, falls eine Bauernumwandlung eines Bauern möglich ist
    if feld[ya][xa] == "B":
        if rn.random() < 0.45: #damit der Computergegner mehr mit den Bauern macht wird der Wert der Züge mit Bauern manchmal erhöht
            bewertung = bewertung + 1
        if ye == 6 and feld[7][xe] == "0": #fast am Ende des Spielfelds
            bewertung = bewertung + 1
        if ye == 7: # am Ende des Spielfelds
            bewertung = bewertung + 3
        if ya == 1 and ye == 3: #Erhöhung der Bewertung, falls ein Bauer 2 Züge machen kann
            bewertung = bewertung + 1
            
        
    if feld[ya][xa] == "b":
        if rn.random() < 0.45: #damit der Computergegner mehr mit den Bauern macht wird der Wert der Züge mit Bauern manchmal erhöht
            bewertung = bewertung + 1
        if ye == 1 and feld[0][xe] == "0": #fast am Ende des Spielfelds
            bewertung = bewertung + 1
        if ye == 0: # am Ende des Spielfelds
            bewertung = bewertung + 3
        if ya == 6 and ye == 4: #Erhöhung der Bewertung, falls ein Bauer 2 Züge machen kann
            bewertung = bewertung + 1
               
    
    #Bewertung aufgrund von Deckung gegenüber einer anderen verbündeten Figur(wichtig: Wertung einge Figur und eigene verbündete Figur)
     #IN BEARBEITUNG
    
    #Verringerung der Bewertung, wenn die Figur aus einer Deckung rausgeht(wichtig: Wertung eigener Figur)
    wertung_fuer_Kriterium = 3 #für den Entwickler -> Verändert Gewichtung 
    eigene_status_deckung, eigene_vielfachheit_deckung, eigene_art_deckung = feld_gedeckt(ya,xa,ya,xa,feld,eigene_farbe)
    if eigene_status_deckung == True:
        bewertung = bewertung - 1
        #if wertung_figur[figur_typ] > 2:
            #bewertung = bewertung - int(wertung_figur[figur_typ]/wertung_fuer_Kriterium) #wird abhänig vom Wert der Figur gemacht
    #Erhöhung der Bewertung , wenn die Figur aus einer Gefahrensituation (feindliche Deckung) rausgeht  
    gegner_status_deckung, gegner_vielfachheit_deckung, gegner_art_deckung = feld_gedeckt(ya,xa,ya,xa,feld,gegner_farbe)

    if gegner_status_deckung == True:
        bewertung = bewertung + 1
        #if wertung_figur[figur_typ] > 2:
            #bewertung = bewertung + int(wertung_figur[figur_typ]/wertung_fuer_Kriterium)
            
    #erstellt Variabel für die Abbruchbedingung der folgenden while Schleife
    evd_schleife = copy.deepcopy(eigene_vielfachheit_deckung)
    #Zieht Wertungspunkte ab, je größer die gegner Deckung im Vergleich zur eigenen ist; desto mehr Wertungspunkte
    while gegner_vielfachheit_deckung > evd_schleife:
        bewertung = bewertung + 1
        evd_schleife = evd_schleife + 1
        #!!! weiter mit Bezug auf den Wert der Figuren, die an der Deckung beteiligt sind
    
    
    #das selbe für den Fall, dass die Deckung der eigenen Figuren besser ist
    gvd_schleife = copy.deepcopy(gegner_vielfachheit_deckung)
    #Fügt Wertungspunkte hinzu, je größer die eigene Deckung im Vergleich zur gegner Deckung ist; desto mehr Wertungspunkte
    while eigene_vielfachheit_deckung > gvd_schleife:
        bewertung = bewertung - 1
        gvd_schleife = gvd_schleife + 1        


    
   #Verringerung der Bewertung, wenn die Figur aus eine Position, in der sie jemanden Schlagen könnte verlässt(wichtig: Wertung der gegnerFigur)
    #IN BEARBEITUNG
    #zu Test-Zwecken:
    print(" ")
    print("eigen",eigene_status_deckung, eigene_vielfachheit_deckung, eigene_art_deckung)
    print("fremd",gegner_status_deckung, gegner_vielfachheit_deckung, gegner_art_deckung)
    print(ya,xa,ye,xe)
    print("bewertung:", bewertung)
    return bewertung


def feld_gedeckt(ya,xa,y,x,feld,farbe):#gibt Informationen zur Deckung der abgefragten Figur zurück /farbe = verbündete Farbe
    
    #Initialisierung der benötigten Variabeln   
    #Variabeln, die später zurückgegeben werden
    status = False
    vielfachheit = 0
    art = []
    
    #schwarze und weiße Figuren
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    
    #benötigte Arrays
    arbeits_feld = copy.deepcopy(feld) #aufgrund von Problemen mit globalen Variabeln
    if farbe == "weiß":
        arbeits_feld[y][x] = "B" #erstellt eine gegnerische Figur auf diesem Feld, damit später die moeglichezuege() - Funktion angewendet werden kann
    else:#== "schwarz"
        arbeits_feld[y][x] = "b"
    arbeits_feld[ya][xa] = "0" #ursprungs-Feld wird geleert 

    eigene_Figuren, eigene_Figuren_typ = alle_eigenen_figuren(arbeits_feld, farbe)
    
    
    for i in range(0,int(len(eigene_Figuren) / 2)):
        #Erstellt in jedem Iterationsschritt ein Array mit den möglichen Zügen einer Figur..dabei verläuft die for-Schleife über jede Figur
        
        mz = (zm.moeglichezuege(eigene_Figuren[i * 2],eigene_Figuren[i * 2 + 1],arbeits_feld,farbe))
        
        #Vergleicht die Koordinaten im Array mit den möglichen Zügen mit der y und x Koordinate, für welches Feld die Deckung überprüft werden soll
        for j in range(0,int(len(mz) / 2)):
            if y == mz[j * 2]:
                if x == mz[j * 2 + 1]:
                    #wenn y und x Koordinate übereinstimmen:
                    #erhöht die Anzahl der Deckungen der Figur
                    vielfachheit = vielfachheit + 1
                    #Hängt den Typen der Figur an das Array "art" an, wenn diese Figur das Feld[y][x] schlagen kann
                    art.append(arbeits_feld[eigene_Figuren[i * 2]][eigene_Figuren[i * 2 + 1]])
    
    
    if vielfachheit > 0:
        #wenn es eine Person gibt, die das Feld[y][x] deckt:
        status = True
    
    return(status, vielfachheit, art)



def alle_eigenen_figuren(feld,farbe):#(getestet)aef_typ_array in Form y1,x1,typ1,y2,x2,typ2,y3,x3.../aef_array in Form y1,x1,y2,x2,....

    aef_array = []
    aef_typ_array = []
    
    
    for y in range(0,8): 
        for x in range(0,8): 
            #wenn alle weißen Figuren gefragt sind:
            if (farbe == "weiß" and feld[y][x] in wF):
                    aef_array.append(y)
                    aef_array.append(x)
                    
                    aef_typ_array.append(y)
                    aef_typ_array.append(x)
                    aef_typ_array.append(feld[y][x])
            
            #wenn alle schwarzen Figuren gefragt sind:
            elif (farbe == "schwarz" and feld[y][x] in sF):
                    aef_array.append(y)
                    aef_array.append(x)
                
                    aef_typ_array.append(y)
                    aef_typ_array.append(x)
                    aef_typ_array.append(feld[y][x])
                    
    return (aef_array, aef_typ_array)
    





