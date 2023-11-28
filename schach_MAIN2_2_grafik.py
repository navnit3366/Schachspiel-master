# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:42:41 2018

@author: Julian Stähle, Sönke Beier
"""
import os
from pylab import *
import schach_ZUG as z
import schach_GRAFIK as grafik
import schach_SETTINGS_SONSTIGES as seso
import schach_CPU as cpu
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import pygame
import webbrowser
import copy
import random

# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Schach")



#Erstellung des 8*8 Arrays des feldes zu Beginn:
feld = np.array(
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

#Intro
os.system("Schach_5.mp4")
fenster.title("Schach | " + einstellungen["Name1"] + " vs. " + einstellungen["Name2"])

#vorgegebene Variabeln die für den Ablauf des Programms benötigt werden
ya = None 
xa = None 
farbe = "weiß" #zeigt die Farbe an,die in diesen Moment an der Reihe ist
status_ablauf = 1 #regelt den Ablauf des Programms



#Vorgang wird ausgeführt, wenn ein Button gedrückt wird
def button_Funktion(y,x):#(fertig)y,x sind columne, row des Buttons
    #GLOBALE VARIABELN WERDEN BENUTZT
    global ya
    global xa
    global farbe
    global status_ablauf
    global feld
    sF = ["T","S","L","D","K","B"] #alle schwarzen Figuren
    wF = ["t","s","l","d","k","b"] #alle weißen Figuren
    
    #erzeugt den Buttonsound
    pygame.mixer.init()
    pygame.mixer.music.load('buttonsound2.wav')
    pygame.mixer.music.play()
    
    #Erster Schritt jedes Zuges 
    if status_ablauf == 1:
        ya = y
        xa = x
        status_ablauf = 2
        
        #Überprüfung ob die gewünschte Figur einem selbst gehört
        if  feld[ya][xa] == "0" :
            messagebox.showerror("Error", "Auf diesem Feld steht keine Figur!")
            status_ablauf = 1
        else:
            if farbe == "weiß":
                if feld[ya][xa] not in wF:
                    print("Die ausgewählte Figur ist nicht ihre - weiß ist am Zug")
                    messagebox.showerror("Error","Diese Ausgewählte Figur ist nicht ihre - Weiß ist am Zug")
                    status_ablauf = 1
            else:#farbe == "schwarz"
                if feld[ya][xa] not in sF: 
                    print("Die ausgewählte Figur ist nicht ihre - schwarz ist am Zug")
                    messagebox.showerror("Error","Diese Ausgewählte Figur ist nicht ihre - Schwarz ist am Zug")
                    status_ablauf = 1
         
            
        
        
    #Zweiter Schritt jedes Zuges
    else:
        #Erstellt ein Zugarray mit den notwendigen Informationen für einen Zug
        zugarray4 = [ya,xa,y,x]
        
        #Erstelt das neue Feld nach dem Zug und erstellt eine Variable, die anzeigt, ob der ausgeführt Zug den Schachregeln entspricht
        test_feld = copy.deepcopy(feld) #aufgrund von Problemen mit der globalen Variabel

        neues_feld, zugkorrekt = z.zug_grafik(test_feld,farbe,zugarray4)

        #Überprüfung ob der Zug korrekt war
        if zugkorrekt == True:
            print("Zug durchgeführt")
            #das aktuelle Spielfeld besitzt nun die Werte des Feldes nach dem durchgeführten Zug
            feld = copy.deepcopy(neues_feld)
        else:
            print("Dieser Zug war nicht korrekt bitte versuchen sie es erneut ",farbe, " ist am Zug")
            messagebox.showerror("Error","Dieser Zug ist ungültig")
        
            
        #Nächster Zug fängt wieder mit Schritt 1 an
        status_ablauf = 1
        #Ändert die Farbe für den nächsten Zug
        if zugkorrekt == True:
            if farbe == "weiß":
                farbe = "schwarz"
            else:
                farbe = "weiß"
            
            print(farbe, " ist am Zug")
        
        
        #Wandelt einen Bauern am Ende des Spielfeld um, wenn dies nötig ist
        schritt2, b_farbe, feld = seso.bauernumwandlung_1(feld,einstellungen["Anzahl_Spieler"])#schaut ob ein Bauer umgewandelt werden muss
        if schritt2 == True :
            if b_farbe == "weiß":
                answer = None
                moegliche_Figuren = ['t','d','s','l']#in diese Figuren kann der Bauer verwandelt werden
                while answer not in moegliche_Figuren:
                    answer = simpledialog.askstring("Input", "In welche Figur soll der Bauer umgewandelt werden?(t,d,s,l)", parent = fenster)
                
                feld = seso.bauernumwandlung_2(feld,answer)#wandelt den Bauer schlussendlich um
                    
            else:
                answer = None
                moegliche_Figuren = ['T','D','S','L']#in diese Figuren kann der Bauer verwandelt werden
                while answer not in moegliche_Figuren:
                    answer = simpledialog.askstring("Input", "In welche Figur soll der Bauer umgewandelt werden?(T,D,S,L)", parent = fenster)
                
                feld = seso.bauernumwandlung_2(feld,answer)#wandelt den Bauer schlussendlich um
        
        
        #Ändert die Anzeige der Buttons
        config()
        #Überprüfung ob das Spiel zuende ist
        if seso.partie_verloren(feld,farbe) == True:
            pygame.mixer.init()
            pygame.mixer.music.load('tada.wav')
            pygame.mixer.music.play()
            messagebox.showinfo("verloren", farbe +  " hat verloren")
        
        
        
        
        #Führt einen möglichen Computerzug durch, wenn die Anzahl der Spieler 1 ist
        if zugkorrekt == True:
            
            if einstellungen["Anzahl_Spieler"] == "1":
                print("Computer führt einen Zug aus")
                #Aufgrund möglicher Fehler mit der globalen Variabel "feld" wird eine deepcopy erstellt und später der Computergegner-Funktion übergeben
                neues_feld_cpu = copy.deepcopy(feld)
                #die Computergegner-Funktion gibt ein Feld zurück, auf welchem ein Zug getätigt wurde
                feld = cpu.cpu_main(neues_feld_cpu,farbe,einstellungen["schwierigkeit"])#als farbe ist gerade nur schwarz möglich
                
                
            
                #Änderung der Farbe nach dem Zug
                if farbe == "weiß":
                    farbe = "schwarz"
                else:
                    farbe = "weiß"
                
                
                #Bauernumwandlung
                schritt2, b_farbe, feld = seso.bauernumwandlung_1(feld,einstellungen["Anzahl_Spieler"])
                if schritt2 == True :
                    if b_farbe == "weiß":
                        answer = None
                        moegliche_Figuren = ['t','d','s','l']
                        while answer not in moegliche_Figuren:
                            answer = simpledialog.askstring("Input", "In welche Figur soll der Bauer umgewandelt werden?(t,d,s,l)", parent = fenster)
                
                        feld = seso.bauernumwandlung_2(feld,answer)
                    
                    else:
                        answer = None
                        moegliche_Figuren = ['T','D','S','L']
                        while answer not in moegliche_Figuren:
                            answer = simpledialog.askstring("Input", "In welche Figur soll der Bauer umgewandelt werden?(T,D,S,L)", parent = fenster)
                
                        feld = seso.bauernumwandlung_2(feld,answer)
                
                #Ändert die Anzeige der Buttons
                config()
                
                #Überprüfung ob das Spiel verloren ist
                if seso.partie_verloren(feld,farbe) == True:
                    pygame.mixer.init()
                    pygame.mixer.music.load('verloren.wav')
                    pygame.mixer.music.play(0)
                    messagebox.showinfo("Verloren", einstellungen["Name1"] + " hat verloren")
                    
    
    
    
    
    


#Aktualisiert die Beschriftung des Buttons
def config():
    gfeld = copy.deepcopy(feld)
    for i in range(0,8):
        for j in range(0,8):
            if gfeld[i][j] == "0":
                gfeld[i][j] = " "
    button1.config(text = gfeld[0][0])
    button2.config(text = gfeld[0][1])
    button3.config(text = gfeld[0][2])
    button4.config(text = gfeld[0][3])
    button5.config(text = gfeld[0][4])
    button6.config(text = gfeld[0][5])
    button7.config(text = gfeld[0][6])
    button8.config(text = gfeld[0][7])
    button9.config(text = gfeld[1][0])
    button10.config(text = gfeld[1][1])
    button11.config(text = gfeld[1][2])
    button12.config(text = gfeld[1][3])
    button13.config(text = gfeld[1][4])
    button14.config(text = gfeld[1][5])
    button15.config(text = gfeld[1][6])
    button16.config(text = gfeld[1][7])
    button17.config(text = gfeld[2][0])
    button18.config(text = gfeld[2][1])
    button19.config(text = gfeld[2][2])
    button20.config(text = gfeld[2][3])
    button21.config(text = gfeld[2][4])
    button22.config(text = gfeld[2][5])
    button23.config(text = gfeld[2][6])
    button24.config(text = gfeld[2][7])
    button25.config(text = gfeld[3][0])
    button26.config(text = gfeld[3][1])
    button27.config(text = gfeld[3][2])
    button28.config(text = gfeld[3][3])
    button29.config(text = gfeld[3][4])
    button30.config(text = gfeld[3][5])
    button31.config(text = gfeld[3][6])
    button32.config(text = gfeld[3][7])
    button33.config(text = gfeld[4][0])
    button34.config(text = gfeld[4][1])
    button35.config(text = gfeld[4][2])
    button36.config(text = gfeld[4][3])
    button37.config(text = gfeld[4][4])
    button38.config(text = gfeld[4][5])
    button39.config(text = gfeld[4][6])
    button40.config(text = gfeld[4][7])
    button41.config(text = gfeld[5][0])
    button42.config(text = gfeld[5][1])
    button43.config(text = gfeld[5][2])
    button44.config(text = gfeld[5][3])
    button45.config(text = gfeld[5][4])
    button46.config(text = gfeld[5][5])
    button47.config(text = gfeld[5][6])
    button48.config(text = gfeld[5][7])
    button49.config(text = gfeld[6][0])
    button50.config(text = gfeld[6][1])
    button51.config(text = gfeld[6][2])
    button52.config(text = gfeld[6][3])
    button53.config(text = gfeld[6][4])
    button54.config(text = gfeld[6][5])
    button55.config(text = gfeld[6][6])
    button56.config(text = gfeld[6][7])
    button57.config(text = gfeld[7][0])
    button58.config(text = gfeld[7][1])
    button59.config(text = gfeld[7][2])
    button60.config(text = gfeld[7][3])
    button61.config(text = gfeld[7][4])
    button62.config(text = gfeld[7][5])
    button63.config(text = gfeld[7][6])
    button64.config(text = gfeld[7][7])
    
 
# Funktionen für die Erstellung des Menüs    
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Sönke Hendrik und Julian Stähle\n\
Date: 03.18\n\
Version: Beta 1.0\n\
Programm: Schach\n\
Info: https://www.overleaf.com/read/khvkmfqjnnjm\n\
Entwicklung: https://github.com/SoenBeier/Schachspiel/tree/master \n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")    
    
def backgroundmusic123():
    text = "\
**********************\n\
Hintergrundmusik:\n\
(1) Tootle Pip (Sims 4)\n\
(2) Crafty Party von Gert Wilden\n\
(3) Spanish Flea von Herb Alpert\n\
(4) Left bank two von Wayne Hill \n\
**********************"
    messagebox.showinfo(message=text,title = "Verwendete Hintergrundmusik")

#öffnet eine website hier für Schachregeln
def webbi():
    
    webbrowser.open_new(r'http://wiki-schacharena.de/index.php/Vollständiges_Regelwerk')    

#Aufgebe - Funktion
def aufgeben():
    text = 'Sie haben Aufgegeben.'
    messagebox.showinfo(message=text, title = "Aufgeben")
    fenster.after(1, sys.exit)
Aufgeben = Button(fenster, text='Aufgeben', command = aufgeben) 
    
# Funktionen für Knöpfe

def Falscherzug():
    messagebox.showerror("Error","Dieser Zug ist ungültig")
    
def Schachmatt1(einstellungen):
    messsagebox.showinfo("Schachmatt", text = einstellungen[Name1]+" hat gewonnen")

def Schachmatt2(einstellungen):
    messagebox.showinfo("Schachmatt", text = einstellungen[Name2]+" hat gewonnen")    
    
     
#Definieren der einzelnen Buttons 

#Randbuchstaben und Zahlen   
Titel = Label(fenster,text = einstellungen["Name1"] + " vs " + einstellungen["Name2"],font=('Georgia',15, "bold underline"), justify = "left")
farb_info = Label(fenster, text = einstellungen["Name1"] + " - weiß - Kleinbuchstaben \n"  + einstellungen["Name2"] + " - schwarz - Großbuchstaben",font=('Georgia',10), justify = "left")
Musikauswahl = Label(fenster, text = "Musikauswahl", font = ('Georgia',20,"bold underline"))
Ziel = Label(fenster, text = "ZIEL : Schlagen Sie alle gegnerischen Figuren!", font = ('Georgia',12))
A = Label(fenster, text = 'A') 
B = Label(fenster, text = 'B')
C = Label(fenster, text = 'C')
D = Label(fenster, text = 'D')
E = Label(fenster, text = 'E')
F = Label(fenster, text = 'F')
G = Label(fenster, text = 'G')
H = Label(fenster, text = 'H')
I = Label(fenster, text = '1')
J = Label(fenster, text = '2')
K = Label(fenster, text = '3')
L = Label(fenster, text = '4')
M = Label(fenster, text = '5')
N = Label(fenster, text = '6')
O = Label(fenster, text = '7')
P = Label(fenster, text = '8')
Titel.place(x = 500, y = 50)
farb_info.place(x = 500, y = 85)
Musikauswahl.place(x = 900, y = 0)
Ziel.place(x=500, y=150)
I.place(x = 400, y=15)
J.place(x = 400, y=65)
K.place(x = 400, y=115)
L.place(x = 400, y=165)
M.place(x = 400, y=215)
N.place(x = 400, y=265)
O.place(x = 400, y=315)
P.place(x = 400, y=365)
A.place(x = 17, y= 400)
B.place(x = 67, y=400)
C.place(x = 117, y=400)
D.place(x = 167, y=400)
E.place(x = 217, y=400)
F.place(x = 267, y=400)
G.place(x = 317, y=400)
H.place(x = 367, y=400)

#Zeile 1
button1 = Button(fenster, text=feld[0][0],bg='white',fg='black',command = lambda: button_Funktion(0,0),font=('Georgia',20))
button2 = Button(fenster, text=feld[0][1],bg='black',fg='white',command = lambda: button_Funktion(0,1),font=('Georgia',20))
button3 = Button(fenster, text=feld[0][2],bg='white',fg='black',command = lambda: button_Funktion(0,2),font=('Georgia',20))
button4 = Button(fenster, text=feld[0][3],bg='black',fg='white',command = lambda: button_Funktion(0,3),font=('Georgia',20))
button5 = Button(fenster, text=feld[0][4],bg='white',fg='black',command = lambda: button_Funktion(0,4),font=('Georgia',20))
button6 = Button(fenster, text=feld[0][5],bg='black',fg='white',command = lambda: button_Funktion(0,5),font=('Georgia',20))
button7 = Button(fenster, text=feld[0][6],bg='white',fg='black',command = lambda: button_Funktion(0,6),font=('Georgia',20))
button8 = Button(fenster, text=feld[0][7],bg='black',fg='white',command = lambda: button_Funktion(0,7),font=('Georgia',20))
#Zeile 2
button9 = Button(fenster, text=feld[1][0],bg='black',fg='white',command = lambda: button_Funktion(1,0),font=('Georgia',20))
button10 = Button(fenster, text=feld[1][1],bg='white',fg='black',command = lambda: button_Funktion(1,1),font=('Georgia',20))
button11 = Button(fenster, text=feld[1][2],bg='black',fg='white',command = lambda: button_Funktion(1,2),font=('Georgia',20))
button12 = Button(fenster, text=feld[1][3],bg='white',fg='black',command = lambda: button_Funktion(1,3),font=('Georgia',20))
button13 = Button(fenster, text=feld[1][4],bg='black',fg='white',command = lambda: button_Funktion(1,4),font=('Georgia',20))
button14 = Button(fenster, text=feld[1][5],bg='white',fg='black',command = lambda: button_Funktion(1,5),font=('Georgia',20))
button15 = Button(fenster, text=feld[1][6],bg='black',fg='white',command = lambda: button_Funktion(1,6),font=('Georgia',20))
button16 = Button(fenster, text=feld[1][7],bg='white',fg='black',command = lambda: button_Funktion(1,7),font=('Georgia',20))
#Zeile 3
button17 = Button(fenster, text=feld[2][0],bg='white',fg='black',command = lambda: button_Funktion(2,0),font=('Georgia',20))
button18 = Button(fenster, text=feld[2][1],bg='black',fg='white',command = lambda: button_Funktion(2,1),font=('Georgia',20))
button19 = Button(fenster, text=feld[2][2],bg='white',fg='black',command = lambda: button_Funktion(2,2),font=('Georgia',20))
button20 = Button(fenster, text=feld[2][3],bg='black',fg='white',command = lambda: button_Funktion(2,3),font=('Georgia',20))
button21 = Button(fenster, text=feld[2][4],bg='white',fg='black',command = lambda: button_Funktion(2,4),font=('Georgia',20))
button22 = Button(fenster, text=feld[2][5],bg='black',fg='white',command = lambda: button_Funktion(2,5),font=('Georgia',20))
button23 = Button(fenster, text=feld[2][6],bg='white',fg='black',command = lambda: button_Funktion(2,6),font=('Georgia',20))
button24 = Button(fenster, text=feld[2][7],bg='black',fg='white',command = lambda: button_Funktion(2,7),font=('Georgia',20))
#Zeile 4
button25 = Button(fenster, text=feld[3][0],bg='black',fg='white',command = lambda: button_Funktion(3,0),font=('Georgia',20))
button26 = Button(fenster, text=feld[3][1],bg='white',fg='black',command = lambda: button_Funktion(3,1),font=('Georgia',20))
button27 = Button(fenster, text=feld[3][2],bg='black',fg='white',command = lambda: button_Funktion(3,2),font=('Georgia',20))
button28 = Button(fenster, text=feld[3][3],bg='white',fg='black',command = lambda: button_Funktion(3,3),font=('Georgia',20))
button29 = Button(fenster, text=feld[3][4],bg='black',fg='white',command = lambda: button_Funktion(3,4),font=('Georgia',20))
button30 = Button(fenster, text=feld[3][5],bg='white',fg='black',command = lambda: button_Funktion(3,5),font=('Georgia',20))
button31 = Button(fenster, text=feld[3][6],bg='black',fg='white',command = lambda: button_Funktion(3,6),font=('Georgia',20))
button32 = Button(fenster, text=feld[3][7],bg='white',fg='black',command = lambda: button_Funktion(3,7),font=('Georgia',20))
#Zeile 5
button33 = Button(fenster, text=feld[4][0],bg='white',fg='black',command = lambda: button_Funktion(4,0),font=('Georgia',20))
button34 = Button(fenster, text=feld[4][1],bg='black',fg='white',command = lambda: button_Funktion(4,1),font=('Georgia',20))
button35 = Button(fenster, text=feld[4][2],bg='white',fg='black',command = lambda: button_Funktion(4,2),font=('Georgia',20))
button36 = Button(fenster, text=feld[4][3],bg='black',fg='white',command = lambda: button_Funktion(4,3),font=('Georgia',20))
button37 = Button(fenster, text=feld[4][4],bg='white',fg='black',command = lambda: button_Funktion(4,4),font=('Georgia',20))
button38 = Button(fenster, text=feld[4][5],bg='black',fg='white',command = lambda: button_Funktion(4,5),font=('Georgia',20))
button39 = Button(fenster, text=feld[4][6],bg='white',fg='black',command = lambda: button_Funktion(4,6),font=('Georgia',20))
button40 = Button(fenster, text=feld[4][7],bg='black',fg='white',command = lambda: button_Funktion(4,7),font=('Georgia',20))
#Zeile 6
button41 = Button(fenster, text=feld[5][0],bg='black',fg='white',command = lambda: button_Funktion(5,0),font=('Georgia',20))
button42 = Button(fenster, text=feld[5][1],bg='white',fg='black',command = lambda: button_Funktion(5,1),font=('Georgia',20))
button43 = Button(fenster, text=feld[5][2],bg='black',fg='white',command = lambda: button_Funktion(5,2),font=('Georgia',20))
button44 = Button(fenster, text=feld[5][3],bg='white',fg='black',command = lambda: button_Funktion(5,3),font=('Georgia',20))
button45 = Button(fenster, text=feld[5][4],bg='black',fg='white',command = lambda: button_Funktion(5,4),font=('Georgia',20))
button46 = Button(fenster, text=feld[5][5],bg='white',fg='black',command = lambda: button_Funktion(5,5),font=('Georgia',20))
button47 = Button(fenster, text=feld[5][6],bg='black',fg='white',command = lambda: button_Funktion(5,6),font=('Georgia',20))
button48 = Button(fenster, text=feld[5][7],bg='white',fg='black',command = lambda: button_Funktion(5,7),font=('Georgia',20))
#Zeile 7
button49 = Button(fenster, text=feld[6][0],bg='white',fg='black',command = lambda: button_Funktion(6,0),font=('Georgia',20))
button50 = Button(fenster, text=feld[6][1],bg='black',fg='white',command = lambda: button_Funktion(6,1),font=('Georgia',20))
button51 = Button(fenster, text=feld[6][2],bg='white',fg='black',command = lambda: button_Funktion(6,2),font=('Georgia',20))
button52 = Button(fenster, text=feld[6][3],bg='black',fg='white',command = lambda: button_Funktion(6,3),font=('Georgia',20))
button53 = Button(fenster, text=feld[6][4],bg='white',fg='black',command = lambda: button_Funktion(6,4),font=('Georgia',20))
button54 = Button(fenster, text=feld[6][5],bg='black',fg='white',command = lambda: button_Funktion(6,5),font=('Georgia',20))
button55 = Button(fenster, text=feld[6][6],bg='white',fg='black',command = lambda: button_Funktion(6,6),font=('Georgia',20))
button56 = Button(fenster, text=feld[6][7],bg='black',fg='white',command = lambda: button_Funktion(6,7),font=('Georgia',20))
#Zeile 8
button57 = Button(fenster, text=feld[7][0],bg='black',fg='white',command = lambda: button_Funktion(7,0),font=('Georgia',20))
button58 = Button(fenster, text=feld[7][1],bg='white',fg='black',command = lambda: button_Funktion(7,1),font=('Georgia',20))
button59 = Button(fenster, text=feld[7][2],bg='black',fg='white',command = lambda: button_Funktion(7,2),font=('Georgia',20))
button60 = Button(fenster, text=feld[7][3],bg='white',fg='black',command = lambda: button_Funktion(7,3),font=('Georgia',20))
button61 = Button(fenster, text=feld[7][4],bg='black',fg='white',command = lambda: button_Funktion(7,4),font=('Georgia',20))
button62 = Button(fenster, text=feld[7][5],bg='white',fg='black',command = lambda: button_Funktion(7,5),font=('Georgia',20))
button63 = Button(fenster, text=feld[7][6],bg='black',fg='white',command = lambda: button_Funktion(7,6),font=('Georgia',20))
button64 = Button(fenster, text=feld[7][7],bg='white',fg='black',command = lambda: button_Funktion(7,7),font=('Georgia',20))

config()
#Erstellt Menü

# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt

datei_menu.add_command(label="Exit", command=fenster.quit)

help_menu.add_command(label="Schachregeln", command = webbi)
help_menu.add_command(label="About...", command=action_get_info_dialog)
help_menu.add_command(label="Hintergrundmusik",command = backgroundmusic123)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
fenster.config(menu=menuleiste)
    
    
#ZUTEILUNG DER BUTTONS : WO GEHÖREN SIE HIN    
#Zeile 1
button1.place(x=0, y=0, width=50, height= 50)
button2.place(x=50, y=0, width=50, height= 50)
button3.place(x=100, y=0, width=50, height= 50)
button4.place(x=150, y=0, width=50, height= 50)
button5.place(x=200, y=0, width=50, height= 50)
button6.place(x=250, y=0, width=50, height= 50)
button7.place(x=300, y=0, width=50, height= 50)
button8.place(x=350, y=0, width=50, height= 50)
#Zeile 2
button9.place(x=0, y=50, width=50, height= 50)
button10.place(x=50, y=50, width=50, height= 50)
button11.place(x=100, y=50, width=50, height= 50)
button12.place(x=150, y=50, width=50, height= 50)
button13.place(x=200, y=50, width=50, height= 50)
button14.place(x=250, y=50, width=50, height= 50)
button15.place(x=300, y=50, width=50, height= 50)
button16.place(x=350, y=50, width=50, height= 50)
#Zeile 3
button17.place(x=0, y=100, width=50, height= 50)
button18.place(x=50, y=100, width=50, height= 50)
button19.place(x=100, y=100, width=50, height= 50)
button20.place(x=150, y=100, width=50, height= 50)
button21.place(x=200, y=100, width=50, height= 50)
button22.place(x=250, y=100, width=50, height= 50)
button23.place(x=300, y=100, width=50, height= 50)
button24.place(x=350, y=100, width=50, height= 50)
#Zeile 4
button25.place(x=0, y=150, width=50, height= 50)
button26.place(x=50, y=150, width=50, height= 50)
button27.place(x=100, y=150, width=50, height= 50)
button28.place(x=150, y=150, width=50, height= 50)
button29.place(x=200, y=150, width=50, height= 50)
button30.place(x=250, y=150, width=50, height= 50)
button31.place(x=300, y=150, width=50, height= 50)
button32.place(x=350, y=150, width=50, height= 50)
#Zeile 5
button33.place(x=0, y=200, width=50, height= 50)
button34.place(x=50, y=200, width=50, height= 50)
button35.place(x=100, y=200, width=50, height= 50)
button36.place(x=150, y=200, width=50, height= 50)
button37.place(x=200, y=200, width=50, height= 50)
button38.place(x=250, y=200, width=50, height= 50)
button39.place(x=300, y=200, width=50, height= 50)
button40.place(x=350, y=200, width=50, height= 50)
#Zeile 6
button41.place(x=0, y=250, width=50, height= 50)
button42.place(x=50, y=250, width=50, height= 50)
button43.place(x=100, y=250, width=50, height= 50)
button44.place(x=150, y=250, width=50, height= 50)
button45.place(x=200, y=250, width=50, height= 50)
button46.place(x=250, y=250, width=50, height= 50)
button47.place(x=300, y=250, width=50, height= 50)
button48.place(x=350, y=250, width=50, height= 50)
#Zeile 7
button49.place(x=0, y=300, width=50, height= 50)
button50.place(x=50, y=300, width=50, height= 50)
button51.place(x=100, y=300, width=50, height= 50)
button52.place(x=150, y=300, width=50, height= 50)
button53.place(x=200, y=300, width=50, height= 50)
button54.place(x=250, y=300, width=50, height= 50)
button55.place(x=300, y=300, width=50, height= 50)
button56.place(x=350, y=300, width=50, height= 50)
#Zeile 8
button57.place(x=0, y=350, width=50, height= 50)
button58.place(x=50, y=350, width=50, height= 50)
button59.place(x=100, y=350, width=50, height= 50)
button60.place(x=150, y=350, width=50, height= 50)
button61.place(x=200, y=350, width=50, height= 50)
button62.place(x=250, y=350, width=50, height= 50)
button63.place(x=300, y=350, width=50, height= 50)
button64.place(x=350, y=350, width=50, height= 50)



#andere buttons
#Patt.place(x=500,y=150,width = 150, height = 50)
Aufgeben.place(x=500,y=250,width = 150, height = 50)
# In der Ereignisschleife auf Eingabe des Benutzers warten.

#Cover am Rand
ltext = "\
Bitte Starten sie den Kernel oder am besten das ganze Programm neu.\n\
\n\
Dieser Error erscheint wenn sie etwas am code geändert haben, ihn ausgeführt haben\
und ein Fehler erscheint. Wenn sie diesen behoben haben und das Programm Starten\
hat Pygame ein Problem damit das Image einzubinden. Wir bitten um Entschuldigung."
try:
    photo = PhotoImage(file ="BS.gif")
    imagelabel= Label(fenster, image = photo)
    imagelabel.place(x=900, y=400, width =200, height=200)
except:
    messagebox.showerror(message = ltext, title = "Image Pygame Error")



#Hintergrundsound im Fenster
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
'''_songs = ["CraftyParty.wav","tootledip.wav"]
_currently_playing_song = None
def soundstop():
    global _currently_playing_song
    _currently_playing_song = None
def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

soundbutton = Button(fenster, text = "Play Backgroundmusic", command = play_a_different_song)
soundbutton.place(x = 900, y = 25)

soundbutton = Button(fenster, text = "Stop Backgroundmusic", command = soundstop)
soundbutton.place(x = 900, y = 75)

'''#spielt random songs aber nicht im Hintergrund

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
sound = pygame.mixer.Sound("tootledip.wav")    
sound2 = pygame.mixer.Sound("CraftyParty.wav")
sound3 = pygame.mixer.Sound("SpanishFlea.wav")
sound4 = pygame.mixer.Sound("leftb2.wav")

soundbutton = Button(fenster, text = "Play tootledip", command = sound.play)
soundbutton.place(x = 900, y = 50)

soundbutton = Button(fenster, text = "Stop tootledip", command = sound.stop)
soundbutton.place(x = 900, y = 100)


soundbutton = Button(fenster, text = "Play Craftyparty", command = sound2.play)
soundbutton.place(x = 1000, y = 50)

soundbutton = Button(fenster, text = "Stop Craftyparty", command = sound2.stop)
soundbutton.place(x = 1000, y = 100)

soundbutton = Button(fenster, text = "Play Spanishflea", command = sound3.play)
soundbutton.place(x = 900, y = 150)

soundbutton = Button(fenster, text = "Stop Spanishflea", command = sound3.stop)
soundbutton.place(x = 900, y = 200)

soundbutton = Button(fenster, text = "Start left bank two", command = sound4.play)
soundbutton.place(x = 1000, y = 150)

soundbutton = Button(fenster, text = "Stop left bank two", command = sound4.stop)
soundbutton.place(x = 1000, y = 200)

fenster.iconbitmap(r'Pferd.ico')




#Mainloop
fenster.mainloop()    
    
    
    
    
    
    
    
