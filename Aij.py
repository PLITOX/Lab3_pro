#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 01:11:07 2021

@author: caelinux
"""

import numpy as np

def Aij(df_i,df_j):
    
    #Zwraca funkcje podcałkowa ->pochodne funckji kształtu 
    #fun_podc = lambda x: -df_i(x)*df_j(x) + c*f_i(x)*f_j(x)
    fun_podc = lambda x: -df_i(x)*df_j(x)
    return fun_podc 