# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:46:56 2018

@author: S.H.B
"""



from pylab import*
import schach_CPU as cpu
import random as rn
import schach_zugMOEGLICHKEITEN as zm
import schach_GRAFIK as g
from tkinter import *
import copy
import schach_GRAFIK


spielfeld = np.array(
    [["T","S","L","D","K","L","S","T"],#0
     ["B","B","B","B","B","B","B","B"],#1
     ["0","0","0","0","0","0","0","0"],#2
     ["0","0","0","0","0","0","0","0"],#3
     ["0","0","0","0","0","0","0","0"],#4
     ["0","0","0","B","0","0","0","0"],#5
     ["b","b","b","b","b","b","b","b"],#6
     ["t","s","l","d","k","l","s","t"]])#7
#      0   1   2   3   4   5   6   7
farbe = "schwarz"
i = 0
ya = 1
xa = 0
ye = 5
xe = 2


print(schach_GRAFIK.brettzeichnen(cpu.cpu_main(spielfeld,"schwarz","normal")))

