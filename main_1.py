#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:36:53 2021

@author: caelinux

"""
import numpy as np
import matplotlib.pyplot as plt

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
print('ELEMENTY')

twb_L = 'D'
twb_P = 'D'
wwb_L = 0
wwb_P = 1

Y = np.zeros((1,n,n))
print(Y)
print('PLIK_3')

#PLIK 3
#xp=xa xk=xb
def generujTabliceGeometrii(WEZLY, ELEMENTY):
    WEZLY, ELEMENTY = generujTabliceGeometrii(xa, xb, n)
    WAR_BRZEGOWE=[xa, xb]
    
# PLIK 4 Funkcja przedstawiajaca geometrie na podstawie zadanych wezow, elementów 

def rysuj_geometrie(ELEMENTY):
    E = np.size(ELEMENTY)        # do zmiennej E przypisuje ilość kolumn z macierzy ELEMENTY
    print(E) 
    i=1                
    for j in range(1,ELEMENTY[1,E]): 
        ep=ELEMENTY(1,j)                    # przypisanie do zmiennej poczatku wspolrzednej elementu
        ek=ELEMENTY(2,j)                    # przypisanie do zmiennej konca wspolrzednej elementu  
        P1=[ep, ek]                          # pomocnicze zmienne do plot
        P2=[0, 0]                            
        plt.plot(ep,0,'X',ek,0,'X',P1,P2)        # rysowanie lini
        plt.show()
        j=j+1
        i=i+1
        print('1')

#rysuj_geometrie(ELEMENTY)


# PLIK 5 Utworzenie zmiennych przechgowujacych meacir4z współczynników i wektórw prawej strony ikładu 

def Alokacja_Pamieci(A,b):
    A = np.zeros(1,n,n) #Utworzenie macierzy n-n wypelnionej zerami;
    b = np.zeros(n,1)
 


# PLIK 6 Generowanie lokalnych fuinckji kształtu funkcjne linowe 

def definicja_funckji_kształtu(fun_ksztaltu):
    i=n-1;
    lokalne_fun_ksztaltu=np.zeros(i,2);
    psi=1;
    #petla dla lokalnej funkcji ksztaltu
    for n in range(1,i):
        lokalne_fun_ksztaltu(n,1)=(-1/2)*psi+(1/2); # wzory z instrukcji
        lokalne_fun_ksztaltu(n,2)=(1/2)*psi+(1/2);
    
  



'''