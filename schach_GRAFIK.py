# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:23:41 2018

@author: S.H.B
"""

from pylab import *

def brettzeichnen(spielfeld):# zeichnet den jetzigen Zustand des Feldes (FEHLT: ABCD usw. am Rand, Lösung: mit print Befehlen)
    print("   ",1," ",2," ",3," ",4," ",5," ",6," ",7," ",8)
    print("A", spielfeld[0][:]) 
    print("B", spielfeld[1][:])
    print("C", spielfeld[2][:])
    print("D", spielfeld[3][:]) 
    print("E", spielfeld[4][:])
    print("F", spielfeld[5][:])
    print("G", spielfeld[6][:])
    print("H", spielfeld[7][:]) 