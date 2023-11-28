# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:31:59 2018

@author: S.H.B
"""

#SETTINGS
def settings(): #(getestet) die Einstellungen des Spiels werden nach Eingabe in einem Dictionary gespeichert
    Name1,Name2,Anzahl = spielernamen()
    einstellungen = {"Name1" : Name1, "Name2" : Name2, "Anzahl_Spieler" : Anzahl, "schwierigkeit" : schwierigkeit_festlegen()}
    #FEHLT: möglichkeit ohne einschränkungen (wie regeln) zu spielen 
    
    return einstellungen


def spielernamen(): #(getestet) gibt die Namen der Spieler in 2 Variabeln (Name1, Name2) zurück, welche zuvor vom Benutzer kreiiert worden sind
    # Spieleranzahlabfrage
    AnzahlderSpieler = None
    moeglichkeiten = ["1","2","3"]
    
    while AnzahlderSpieler not in moeglichkeiten:
        AnzahlderSpieler = (input("Anzahl der Spieler? "))
        if AnzahlderSpieler == "1":
            Name1 = input("Ich bin ",)
            Name2 = "CPU"
            print("Hallo",Name1,"und viel Spaß beim Spielen ")
        elif AnzahlderSpieler == "2":
            Name1 = input("Spieler 1 heißt ")
            Name2 = input("Spieler 2 heißt ")
            print("Hallo",Name1,"und",Name2,". Viel Spaß beim Spielen")
        elif AnzahlderSpieler == "0":
            Name1 = "CPU1"
            Name2 = "CPU2"
        else :
            print("Bitte eine gültige Anzahl an Spielern eintragen(0,1 oder 2 )")
    return (Name1,Name2,AnzahlderSpieler) #gibt die Namen der Spieler zurück

def schwierigkeit_festlegen():
    schwierigkeit = None
    moeglichkeiten = ["leicht","normal","schwer"]
    
    while schwierigkeit not in moeglichkeiten:
        schwierigkeit = input("Schwierigkeit auswählen(leicht,normal)")
    
    return(schwierigkeit)
        

#SONSTIGES
def schachmatt():
    return False

def bauernumwandlung_1(feld,Anzahl_Spieler):#überprüft ob eine Figur in einen Bauern umgewandelt werden muss bzw. wandelt einen Bauern in eine Dame um, wenn der CPU am Zug ist
    schritt2 = False
    b_farbe = None

    #für weiß:
    for i in range(0,8):
        y = 0
        if feld[y][i] == 'b':
            schritt2 = True
            b_farbe = "weiß"
            
               
    #für schwarz:
    for i in range(0,8):
        y = 7
        if feld[y][i] == 'B':
            if Anzahl_Spieler == "1":
                feld[y][i] = "D"
            else:
                schritt2 = True
                b_farbe = "schwarz"
               
    return (schritt2, b_farbe, feld)

def bauernumwandlung_2(feld,figur_wahl):#wandelt den Bauern in die gewünschte Figur um

    #für weiß:
    for i in range(0,8):
        y = 0
        if feld[y][i] == 'b':
            feld[y][i] = figur_wahl
    #für schwarz:
    for i in range(0,8):
        y = 7
        if feld[y][i] == 'B':
            feld[y][i] = figur_wahl
    
    return (feld)
    
    




def partie_verloren(feld,farbe):#gibt True zurück, wenn das Spiel fertig ist
    
    import schach_CPU as cpu
    
    
    #Wenn keine Figuren dieser Farbe auf dem Feld sind hat diese Farbe verloren
    if len(cpu.alle_eigenen_figuren(feld,farbe)) == 0:
        return True
    elif len(cpu.alle_moeglichen_zuege(feld,farbe,"leicht")) == 0:
        return True
    else:
        return False

                
            
    





