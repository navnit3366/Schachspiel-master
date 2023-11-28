# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:52:00 2018

"""

from pylab import *
import schach_ZUG as z
import schach_GRAFIK as grafik
import schach_SETTINGS_SONSTIGES as seso

spielfertig = False
Name1 = "Spieler1" 
Name2 = "Spieler2"

#Erstellung des 8*8 Arrays des Spielfeldes zu Beginn:
spielfeld = np.array(
    [["T","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])
    
#Erstellt ein Dictionary ("Einstellungen" mit den vorgefassten Optionen)
einstellungen = seso.settings() 

while spielfertig == False: #so lange spielfertig == False, läuft das Spiel
    
    #Zug von Weiß:
    print("Weiß ist am Zug (b,d,k,t,..)")
    grafik.brettzeichnen(spielfeld)
    
    spielfeld = z.zug(spielfeld, "weiß") #weiß == klein
    
    if seso.schachmatt() == True:
        gewinner = einstellungen["Spieler1"] 
        break
    seso.bauernumwandlung(spielfeld)#Wandelt Bauern um, wenn diese das Ende des Spielfelds erreicht haben
    
    #Zug von Schwarz
    print("Schwarz ist am Zug (B,D,K,T,..)")
    grafik.brettzeichnen(spielfeld)
    spielfeld = z.zug(spielfeld, "schwarz") #schwarz == groß
    if seso.schachmatt() == True:
        gewinner = einstellungen.Spieler2
        break
    seso.bauernumwandlung(spielfeld)
    



