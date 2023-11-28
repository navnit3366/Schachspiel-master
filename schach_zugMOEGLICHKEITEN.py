# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:09:59 2018

@author: S.H.B
"""
#NOCH IM SCHACH STEHEN ERGÄNZEN !!!!
import schach_CPU as cpu

def moeglichezuege(y, x, feld, farbe): 
    #x,y == 0-7 /gibt ein Array zurück, in dem alle möglichen Züge der Figur auf der Position x,y gespeichert sind
    #Zur Erinnerung: Weiß == kleine Buchstaben, Schwarz == große Buchstaben
    m = []#nach und nach werden hier alle möglichen Züge der Figur mit den Koordinaten x,y gespeichert 
    # -> diese sind gespeichert in der der Form [yZiel1,xZiel1,yZiel2,xZiel2,...,yZieln,xZieln]
    
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    aF = sF + wF
    
    #print(feld[y][x])
    
    #y von oben nach unten, x links nach rechts
    # Weiß spielt nach oben, Schwarz spielt nach unten
    
    #Mit if - Abfragen wird geklärt, welche Figur ausgewählt wird:
    
    #Bauer, der Farbe weiß (getestet):
    if feld[y][x] == "b" and farbe == "weiß":#Bauer, kann nur nach oben
        if y != 0 and feld[y-1][x] == "0": #wenn das obere Feld leer ist
            m.append(y - 1)
            m.append(x)
            
            if y == 6 and feld[y-2][x] == "0":#zweier Sprung möglich, wenn noch am ursprünglichen Platz und Ziel frei
                m.append(y - 2)
                m.append(x)
                
        if x != 0 and y != 0 and (feld[y - 1][x - 1] in sF):#Schlag nach Links
            m.append(y - 1)
            m.append(x - 1)
        
        if x != 7 and y != 0 and (feld[y - 1][x + 1] in sF):#Schlag nach Rechts
            m.append(y - 1)
            m.append(x + 1)
        
    #Bauer, der Farbe schwarz (getestet):    
    elif feld[y][x] == "B" and farbe == "schwarz":#Bauer, kann nur nach unten
        if y != 7 and feld[y+1][x] == "0": #wenn das untere Feld leer ist
            m.append(y + 1)
            m.append(x)
            
            if y == 1 and feld[y+2][x] == "0":#zweier Sprung möglich, wenn noch am ursprünglichen Platz und Ziel frei
                m.append(y + 2)
                m.append(x)
                
        if x != 0 and y != 7 and (feld[y + 1][x - 1] in wF): #Schlag nach Links
            m.append(y + 1)
            m.append(x - 1)
        
        if x != 7 and y != 7 and (feld[y + 1][x + 1] in wF): #Schlag nach Rechts
            m.append(y + 1)
            m.append(x + 1)
                
        
        
    #Turm (getestet):    
    elif feld[y][x] == "T" or feld[y][x] == "t" :
        
        if farbe == "weiß": # == klein:
            GegnerFiguren = sF
        else : #Farbe == "schwarz" == groß
            GegnerFiguren = wF
            
        i = y + 1 #es wird mit der nächsten Position begonnen 
        while i <= 7:
            if feld[i][x] in GegnerFiguren:#Schlag auf "y-Reihe" -> von der Figur nach unten
                m.append(i)
                m.append(x)
            if feld[i][x] in aF:
                break
            else:#mögliche Bewegungszüge auf "y-Reihe" ->von der Figur nach unten
                m.append(i)
                m.append(x) 
                i = i + 1
                
        i = y - 1 
        while i >= 0:
            if feld[i][x] in GegnerFiguren:#Schlag auf "y-Reihe" -> von der Figur nach oben
                m.append(i)
                m.append(x)
            if feld[i][x] in aF:
                break
            else:#mögliche Bewegungszüge auf "y-Reihe" ->von der Figur nach oben
                m.append(i)
                m.append(x) 
                i = i - 1
            
        i = x + 1
        while i <= 7:
            if feld[y][i] in GegnerFiguren:#Schlag auf "x-Reihe" -> von der Figur nach rechts
                m.append(y)
                m.append(i)
            if feld[y][i] in aF: #Die Schleife wird unterbrochen, wenn der Turm auf eine Figur trifft
                break
            else: #mögliche Bewegungszüge (ohne Schlagen) auf "x-Achse" -> von der Figur nach rechts
                m.append(y)
                m.append(i) 
            i = i + 1
        
        
        i = x - 1
        while i >= 0:
            if feld[y][i] in GegnerFiguren:#Schlag auf "y-Reihe" -> von der Figur nach links
                m.append(y)
                m.append(i)
            if feld[y][i] in aF:
                break
            else:#mögliche Bewegungszüge auf "y-Reihe" -> von der Figur nach links
                m.append(y)
                m.append(i) 
            i = i - 1
                
            
        
      
    #Springer(getestet):    
    elif feld[y][x] == "S" or feld[y][x] == "s" :
        if farbe == "weiß": # == klein:
            Gegnerund0 = sF + ["0"]
        else : #Farbe == "schwarz" == groß
            Gegnerund0 = wF + ["0"]
        
        if ((y + 2) <= 7 and (x + 1) <= 7): #Schlag oder Bewegung unten2 rechts1
            if feld[y + 2][x + 1] in Gegnerund0 :
                m.append(y + 2)
                m.append(x + 1)
        if ((y + 2) <= 7 and (x - 1) >= 0): #Schlag oder Bewegung unten2 links1 
            if feld[y + 2][x - 1] in Gegnerund0:
                m.append(y + 2)
                m.append(x - 1)
        if ((y - 2) >= 0 and (x + 1) <= 7): #Schlag oder Bewegung oben2 rechts1
            if feld[y - 2][x + 1] in Gegnerund0:
                m.append(y - 2)
                m.append(x + 1)
        if ((y - 2) >= 0 and (x - 1) >= 0): #Schlag oder Bewegung oben2 links1
            if feld[y - 2][x - 1] in Gegnerund0:
                m.append(y - 2)
                m.append(x - 1)
        if ((y + 1) <= 7 and (x + 2) <= 7): #Schlag oder Bewegung unten1 rechts2
            if feld[y + 1][x + 2] in Gegnerund0 :
                m.append(y + 1)
                m.append(x + 2)
        if ((y + 1) <= 7 and (x - 2) >= 0): #Schlag oder Bewegung unten1 links2
            if feld[y + 1][x - 2] in Gegnerund0:
                m.append(y + 1)
                m.append(x - 2)
        if ((y - 1) >= 0 and (x + 2) <= 7): #Schlag oder Bewegung oben1 rechts2
            if feld[y - 1][x + 2] in Gegnerund0:
                m.append(y - 1)
                m.append(x + 2)
        if ((y - 1) >= 0 and (x - 2) >= 0): #Schlag oder Bewegung oben1 links2
            if feld[y - 1][x - 2] in Gegnerund0:
                m.append(y - 1)
                m.append(x - 2)
                
    #Läufer(getestet):
    elif feld[y][x] == "L" or feld[y][x] == "l" :
        if farbe == "weiß": # == klein:
            Gegnerund0 = sF + ["0"]
        else : #Farbe == "schwarz" == groß
            Gegnerund0 = wF + ["0"]
            
            
        # i und j sind die Zählvariabeln: 
        
        # Züge nach rechts unten:
        i = y + 1 #überprüft das nächste Feld und nicht das Feld selbst
        j = x + 1
        while i <= 7 and j <= 7: 
            if feld[i][j] in Gegnerund0: 
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: #wenn die Reihe eine Figur trifft, sind die Positionen keine Möglichkeiten mehr-> deshalb break
                break
            i = i + 1 #geht ein Feld weiter
            j = j + 1
        
        # Züge nach rechts oben
        i = y - 1
        j = x + 1
        while i >= 0 and j <= 7:
            if feld[i][j] in Gegnerund0:
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: 
                break
            i = i - 1
            j = j + 1
        
        # Züge nach links unten
        i = y + 1
        j = x - 1
        while i <= 7 and j >= 0:
            if feld[i][j] in Gegnerund0:
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: 
                break
            i = i + 1
            j = j - 1
        
        # Züge nach links oben
        i = y - 1
        j = x - 1
        while i >= 0 and j >= 0:
            if feld[i][j] in Gegnerund0:
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: 
                break
            i = i - 1
            j = j - 1
        
            
    #Dame(getestet):
    elif feld[y][x] == "D" or feld[y][x] == "d" :
        if farbe == "weiß": # == klein:
            GegnerFiguren = sF
            Gegnerund0 = sF + ["0"]
        else : #Farbe == "schwarz" == groß
            GegnerFiguren = wF
            Gegnerund0 = wF + ["0"]
    # Code für den Läufer / Turm:
            
        # i und j sind die Zählvariabeln: 
        
        # Züge nach rechts unten:
        i = y + 1 #überprüft das nächste Feld und nicht das Feld selbst
        j = x + 1
        while i <= 7 and j <= 7: 
            if feld[i][j] in Gegnerund0: 
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: #wenn die Reihe eine Figur trifft, sind die Positionen keine Möglichkeiten mehr-> deshalb break
                break
            i = i + 1 #geht ein Feld weiter
            j = j + 1
        
        # Züge nach rechts oben
        i = y - 1
        j = x + 1
        while i >= 0 and j <= 7:
            if feld[i][j] in Gegnerund0:
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: 
                break
            i = i - 1
            j = j + 1
        
        # Züge nach links unten
        i = y + 1
        j = x - 1
        while i <= 7 and j >= 0:
            if feld[i][j] in Gegnerund0:
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: 
                break
            i = i + 1
            j = j - 1
        
        # Züge nach links oben
        i = y - 1
        j = x - 1
        while i >= 0 and j >= 0:
            if feld[i][j] in Gegnerund0:
                m.append(i)
                m.append(j)
            if feld[i][j] in aF: 
                break
            i = i - 1
            j = j - 1
        
        #JETZT Turm
        i = y + 1 #es wird mit der nächsten Position begonnen 
        while i <= 7:
            if feld[i][x] in GegnerFiguren:#Schlag auf "y-Reihe" -> von der Figur nach unten
                m.append(i)
                m.append(x)
            if feld[i][x] in aF:
                break
            else:#mögliche Bewegungszüge auf "y-Reihe" ->von der Figur nach unten
                m.append(i)
                m.append(x) 
                i = i + 1
                
        i = y - 1 
        while i >= 0:
            if feld[i][x] in GegnerFiguren:#Schlag auf "y-Reihe" -> von der Figur nach oben
                m.append(i)
                m.append(x)
            if feld[i][x] in aF:
                break
            else:#mögliche Bewegungszüge auf "y-Reihe" ->von der Figur nach oben
                m.append(i)
                m.append(x) 
                i = i - 1
            
        i = x + 1
        while i <= 7:
            if feld[y][i] in GegnerFiguren:#Schlag auf "x-Reihe" -> von der Figur nach rechts
                m.append(y)
                m.append(i)
            if feld[y][i] in aF: #Die Schleife wird unterbrochen, wenn der Turm auf eine Figur trifft
                break
            else: #mögliche Bewegungszüge (ohne Schlagen) auf "x-Achse" -> von der Figur nach rechts
                m.append(y)
                m.append(i) 
            i = i + 1
        
        
        i = x - 1
        while i >= 0:
            if feld[y][i] in GegnerFiguren:#Schlag auf "y-Reihe" -> von der Figur nach links
                m.append(y)
                m.append(i)
            if feld[y][i] in aF:
                break
            else:#mögliche Bewegungszüge auf "y-Reihe" -> von der Figur nach links
                m.append(y)
                m.append(i) 
            i = i - 1
    
    
    #König(getestet)#ROCHADE HINZUFÜGEN, wenn alles auf Spyder übertragen wurde
    elif feld[y][x] == "K" or feld[y][x] == "k" :
        if farbe == "weiß": # == klein:
            GegnerFiguren = sF
            Gegnerund0 = sF + ["0"]
        else : #Farbe == "schwarz" == groß
            GegnerFiguren = wF
            Gegnerund0 = wF + ["0"]
       
        if y < 7:
            if (feld[y + 1][x] in Gegnerund0) and ((y + 1) <= 7): #Feld unten
                if genugabstandkönige(y + 1,x,farbe,feld) == True:#überprüft ob nach diesem Zug der Abstand der Könige noch größer als 1 ist
                    m.append(y + 1)
                    m.append(x)
        if x < 7:
            if (feld[y][x + 1] in Gegnerund0) and ((x + 1) <= 7): #Feld rechts
                print(y,x+1,farbe,feld)
                if genugabstandkönige(y,x + 1,farbe,feld) == True:
                    m.append(y)
                    m.append(x + 1)
        if (y < 7 and x < 7):
            if (feld[y + 1][x + 1] in Gegnerund0) and ((y + 1) <= 7) and ((x + 1) <= 7): #Feld rechts unten
                if genugabstandkönige(y + 1,x + 1,farbe,feld) == True:
                    m.append(y + 1)
                    m.append(x + 1)
        if (y > 0 and x > 0):
            if (feld[y - 1][x - 1] in Gegnerund0) and ((y - 1) >= 0) and ((x - 1) >=0): #Feld links oben  
                if genugabstandkönige(y - 1,x - 1,farbe,feld) == True:
                    m.append(y - 1)
                    m.append(x - 1)
        if y > 0:
            if (feld[y - 1][x] in Gegnerund0) and ((y - 1) >= 0): #Feld oben
                if genugabstandkönige(y - 1,x,farbe,feld) == True:
                    m.append(y - 1)
                    m.append(x)
        if x > 0:
            if (feld[y][x - 1] in Gegnerund0) and ((x - 1) >=0): #Feld links
                if genugabstandkönige(y,x - 1,farbe,feld) == True:
                    m.append(y)
                    m.append(x - 1)
        if (y < 7 and x > 0):
            if (feld[y + 1][x - 1] in Gegnerund0) and ((y + 1) <= 7) and ((x - 1) >=0):#Feld links unten
                if genugabstandkönige(y + 1,x - 1,farbe,feld) == True:
                    m.append(y + 1)
                    m.append(x - 1)
        if (y > 0 and x < 7):
            if (feld[y - 1][x + 1] in Gegnerund0) and ((y - 1) >= 0) and ((x + 1) <= 7): #Feld oben rechts
                if genugabstandkönige(y - 1,x + 1,farbe,feld) == True:
                    m.append(y - 1)
                    m.append(x + 1)
            
    elif feld[y][x] == "0":#Wenn ein lehres Feld aufgerufen wird wird [] zurückgegeben
        return([])
    
    else: #Fehlermeldung
        print(feld[y][x],farbe)
        raise NameError("Error - Schwerwiegender Fehler in moeglichezuege(x,y,feld,farbe) - Figur nicht erkannt")
        
    return m


def genugabstandkönige (y,x,farbe,feld): # (getestet) bekommt y - des Königs, x - des Königs, Farb - Wert des abgefragten Königs und Spielfeld
    '''
    if farbe == "schwarz":
        for a in range(0,8):
            for b in range(0,8):
                if feld[a][b] == "k": 
                    ykK = a #Abstand auf y-Achse könig-König
                    xkK = b #Abstand auf x-Achse könig-König
                    
                                    
    else:  
        for a in range(0,8):
            for b in range(0,8):
                if feld[a][b] == "K": 
                    ykK = a
                    xkK = b
                    
        
    if (abs(y - ykK) > 1) or (abs(x - xkK) > 1): #wenn der Abstand zwischen den y und x Werten der Könige größer als 1 ist, dann ist das in ordnung : return(True)
        genug = True
    else:
        genug = False
    '''
    genug = True
    return (genug) 


def alle_ziele(feld, farbe):#Gibt alle möglichen Ziele der eigenen Figuren wieder; Form :(y1,x1,y2,x2,y3,x3...)
    eigene_Figuren, eigene_Figuren_typ = cpu.alle_eigenen_figuren(feld,farbe)
    #print(eigene_Figuren)
    alle_ziele_array = []
    
    for i in range(0,int(len(eigene_Figuren) / 2)): #geht jede eigene Figur durch
        alle_ziele_array.append(moeglichezuege(eigene_Figuren[i * 2],eigene_Figuren[i * 2 + 1],feld,farbe))#fügt jedes Array, welches die moeglichenzuege erstellt dem alle_ziele_array hinzu
    
    return alle_ziele_array
    
   
    
    