# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:37:24 2019

@author: natanael
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random as ra

n=4
#suffels=5
Boys=np.zeros((n,n))
Girls=np.zeros((n,n))
Match=np.zeros((n))
Rang=np.zeros((n))
Repeat=np.zeros((n))
Match1=np.zeros((n))
Rang1=np.zeros((n))

def crear_matriu_inicial(n):
    Matrix=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            Matrix[i][j]=j

    for i in range(0,n):
        #Rand1=suffels*n
        for j in range(0,n):
            Rand2=int((n-1)*ra.random())
            g1=int(Matrix[i][j])
            g2=int(Matrix[i][Rand2])
            Matrix[i][Rand2]=g1
            Matrix[i][j]=g2
    for i in range(0,n):
        for j in range(0,n):
            Matrix[i][j]=Matrix[i][j]+1
    return Matrix

def Match_Rang_creation(Boys, Girls, n):

    for i in range(0,n):
        k = int(Boys[i][1])
        for q in range(0,n):
            w = int(Girls[k-1][q])-1
            if(w == i):
                Match[i]=k
                Rang[i]=q+1

def totes_diferents(V, n):
    k=0
    for i in range(0,n):
        r=i+1
        for j in range(r,n):
            if(V[i]==V[j]):
                k=1
                return 1
                break
        if(k==1):
            break
def Rango(Girls, n, girl, boy):
    for j in range(0,n):
        if(Girls[boy][j]==girl):
            return j

def zero_repeat(n):
    for i in range(0,n):
        Repeat[i]=0

def comparar(Boys, Girls, n):
    
    Match_Rang_creation(Boys, Girls, n)
    
    for j in range(0,n-1):
        h=totes_diferents(Match, n)
        if(h!=1):
            break
        zero_repeat(n)        
        for i in range(0,n):
            for g in range(0,n):
                if(g==i or Repeat[g]==1):
                    continue
                elif(Match[i]==Match[g]):
                    if(Rang[i]>Rang[g]):
                        Match[i]=Boys[i][j+1]
                        Rang[i]=Rango(Girls, n, int(Match[i]), i)
                        Repeat[i]=1
                        break

    return Match
def main():
    Boys=crear_matriu_inicial(n)
    Girls=crear_matriu_inicial(n)
    print(Boys)
    print(Girls)
    
    
    Match=comparar(Boys, Girls, n)
    print(Rang)
    print(Match)
    
    
main()


