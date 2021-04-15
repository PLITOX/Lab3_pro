#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:36:53 2021

@author: caelinux

"""
import numpy as np
def parametry_sterujace():
    global xa 
    global xb 
    global c 
    global f 
    global n 
    global le
    xa = 0;     #warunek brzegowy 1#liczba wezlow
    xb = 1;     #warunek brzegowy 2
    c = 0;      #sprezystosc
    f = 0;      #sila dzialajaca na obiekt 
    n = 100;    #liczba wezlow
    le = n - 1  #liczba elemntow
    print("Test")

parametry_sterujace()

print(n)
print(le)

WEZLY = np.array([[1, 0], [2, 1], [3, 0.5], [4, 0.75]])
print(WEZLY)

ELEMENTY = np.array([[1, 1, 3], [2, 4, 2], [3, 3, 4]])
print(ELEMENTY)


Y = np.zeros((1,100,100))
print(Y)