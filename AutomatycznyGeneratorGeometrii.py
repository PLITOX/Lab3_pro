#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 00:57:24 2021

@author: caelinux
"""

import numpy as np

def AutomatycznyGeneratorGeometrii(a,b,n):
    '''
    Parametry: 
    a,b - krance przedzialu 
    n - liczba równomiernie rozmieszczoinych wezlow
    zwraca: wezly elementy
    '''
    
    lp = np.arange(1,n+1)
    x = np.linespace(a,b,n) ;
    WEZLY = (np.vstack( (lp.T, x.T) )).T  #[lp.T, x.T]
    
    lp = np.arange(1,n)
    C1 = np.arange(1,n)
    C2 = np.arange(2, n+1)
    ELEMENTY = (np.block( [[lp], [C1], [C2] ] ) ).T
    
    return WEZLY, ELEMENTY