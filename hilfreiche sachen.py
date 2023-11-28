# -*- coding: utf-8 -*-
#hilfreiche Sachen


#Vorspannvideo
def snd1():
    os.system(r"C:\Users\Julian\Desktop\Schach\Schach_5.mp4")
snd1()

#Logo im Spielfenster
a = PhotoImage(file=r"C:\Users\Julian\Desktop\Schach\BS.gif")
imagelabel= Label(fenster, image = a)
imagelabel.place(x=1050, y=25, width =200, height=200)





#öffnet eine website hier für Schachregeln
def webbi():
    
    webbrowser.open_new(r'http://wiki-schacharena.de/index.php/Vollständiges_Regelwerk')

#sounds

def sound1():
    os.system(r'C:\Users\Julian\Music\Parov_Stelar_The_Invisible_Girl.mp3')

audio = Button(fenster,text = 'Hier spielt die Musik',command = sound1, bg='yellow')
audio.place(x = 500, y =0, width = 150, height = 50)


# Funktionen für Knöpfe

def Falscherzug():
    messagebox.showerror("Error","Dieser Zug ist ungültig")
    
def Schachmatt1(einstellungen):
    messsagebox.showinfo("Schachmatt", text = einstellungen[Name1]+" hat gewonnen")

def Schachmatt2(einstellungen):
    messagebox.showinfo("Schachmatt", text = einstellungen[Name2]+" hat gewonnen") 
    

#Stoppuhr

def uhr(fenster, label, second):

    if second <= 60:
        label.configure(text = str(second))
        second += 1
        fenster.after(1000, lambda: uhr(fenster, label, second))
        
label = Label(fenster, text = " ")
label.place(x = 500, y = 400)
button = Button(fenster, text = "Stoppuhr - Start", command = lambda: uhr(fenster, label, 0))
button.place(x = 500, y = 300)


# Save und Load des Feldes in eine dat datei
def save():
    filedialog.asksaveasfilename()
def load():
    filedialog.askopenfilename()
    
def data(feld):
    f = open(r'C:\Users\Julian\Desktop\feld.dat','wb')
    f.write(feld)
    f.close()

#Zeile 1
button1 = Button(fenster, text=feld[0][0],bg='white',fg='black',command = lambda: button_Funktion(0,0),font=('Georgia',20))
button2 = Button(fenster, text=feld[0][1],bg='black',fg='white',command = lambda: button_Funktion(0,1),font=('Georgia',20))
button3 = Button(fenster, text=feld[0][2],bg='white',fg='black',command = lambda: button_Funktion(0,2),font=('Georgia',20))
button4 = Button(fenster, text=feld[0][3],bg='black',fg='white',command = lambda: button_Funktion(0,3),font=('Georgia',20))
button5 = Button(fenster, text=feld[0][4],bg='white',fg='black',command = lambda: button_Funktion(0,4),font=('Georgia',20))
button6 = Button(fenster, text=feld[0][5],bg='black',fg='white',command = lambda: button_Funktion(0,5),font=('Georgia',20)
button7 = Button(fenster, text=feld[0][6],bg='white',fg='black',command = lambda: button_Funktion(0,6),font=('Georgia',20)
button8 = Button(fenster, text=feld[0][7],bg='black',fg='white',command = lambda: button_Funktion(0,7),font=('Georgia',20)
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



    
    
    
    
    
fenster.iconbitmap(r'C:\Users\Julian\Desktop\Pferd.ico')