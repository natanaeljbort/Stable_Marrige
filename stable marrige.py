"""
Created on Wed Nov 27 15:37:24 2019

@author: Natanael
"""

import numpy as np
import random as ra

n=100
Boys=np.zeros((n,n))
Girls=np.zeros((n,n))
Match=np.zeros((n))
M=np.zeros((n))
Rang=np.zeros((n))
Repeat=np.zeros((n))
contador=np.zeros((n))

#Function that creates random matrices in order to have initial testing data .
def crear_matriu_inicial(n):
    Matrix=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            Matrix[i][j]=j

    for i in range(0,n):
        for j in range(0,n):
            Rand2=int((n-1)*ra.random())
            g1=int(Matrix[i][j])
            g2=int(Matrix[i][Rand2])
            Matrix[i][Rand2]=g1
            Matrix[i][j]=g2
    for i in range(0,n):
        for j in range(0,n):
            Matrix[i][j]=Matrix[i][j]
    return Matrix

#Function that creates the initial Match and Rang vectors, which will be modified as the algorithm progresses.
def Match_Rang_creation(Boys, Girls, n):

    for i in range(0,n):
        k = int(Boys[i][0])
        for q in range(0,n):
            w = int(Girls[k][q])
            if(w == i):
                Match[i]=k
                Rang[i]=q
                
#Function that tells us when the solution is found (everybody has a different partner).
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
        
#Function that tells us the rang that a boy has for a given girl.
def Rango(Girls, n, girl, boy):
    for j in range(0,n):
        if(Girls[girl][j]==boy):
            return j

#Function that creates a vector wich tells us with how many boys a girl is paired.
def Contador(Match, n, contador):
    for j in range(0,n):
        k=int(Match[j]);
        contador[k]=contador[k]+1;
    
#Function that finds the solution given the two initial matrices of boys and girls. This is done by modifying the Match ang Rang vector by comparing between the preferences of all the boys and girls.
def comparar(Boys, Girls, n):
    
    Match_Rang_creation(Boys, Girls, n)
    
    for j in range(0,n-1):
        h=totes_diferents(Match, n)
        if(h!=1):
            break      
        for i in range(0,n):
            for g in range(0,n):
                if(g==i):
                    continue
                elif(Match[i]==Match[g] and Rang[i]>Rang[g]):
                    Match[i]=Boys[i][j+1]
                    Rang[i]=Rango(Girls, n, int(Match[i]), i)
                    break

#With the 'comparar' function it may happen that two boys pair the same girl and one girl my be left unpaired (in the last step), this function solves this problem by pairing the most diaired girl with the better ranked boy and the other boy goes with the unpaired girl.
def ultimes_parelles(contador, Match, Rango, n):
    h=totes_diferents(Match, n)
    tiazero=0; tiados=0; tio1=0; tio2=0
    if h==1:
        Contador(Match, n, contador)
        for j in range(0,n):
            if contador[j]==2:
                tiados=j
            elif contador[j]==0:
                tiazero=j
        for j in range(0,n):
            if Match[j]==tiados:
                tio1=j
                break
        for j in range(tio1,n):
            if Match[j]==tiados:
                tio2=j
        if Rang[tio1]>Rang[tio2]:
            Match[tio2]=tiazero
        elif Rang[tio1]<Rang[tio2]:
            Match[tio1]=tiazero
         
    return Match

#Main function.
def main():
    Boys=crear_matriu_inicial(n)
    print("\n The preference matix for the boys is:")
    print(Boys)
    print("\n The preference matix for the girls is:") 
    Girls=crear_matriu_inicial(n)
    print(Girls)   
    comparar(Boys, Girls, n)
    M=ultimes_parelles(contador, Match, Rango, n)
    print("\n The rang vector is: ")
    print(Rang)
    print("\n The Match vector is: ")
    print(M)    
    
main()
