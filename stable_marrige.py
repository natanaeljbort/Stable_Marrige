"""
Created on Wed Nov 27 15:37:24 2019

@author: Natanael
"""

import numpy as np
import random as ra

n=30
Teams=np.zeros((n,n))
Players=np.zeros((n,n))
Match=np.zeros((n))
M=np.zeros((n))
Rang=np.zeros((n))
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
def Match_Rang_creation(Teams, Players, n):

    for i in range(0,n):
        k = int(Teams[i][0])
        for q in range(0,n):
            w = int(Players[k][q])
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
        
#Function that tells us the rang that a team has for a given player.
def Rango(Players, n, player, team):
    for j in range(0,n):
        if(Players[player][j]==team):
            return j

#Function that creates a vector wich tells us with how many Teams a player is paired with.
def Contador(Match, n, contador):
    for j in range(0,n):
        k=int(Match[j]);
        contador[k]=contador[k]+1;
    
#Function that finds the solution given the two initial matrices of Teams and Players. This is done by modifying the Match ang Rang vector by comparing between the preferences of all the Teams and Players.
def comparar(Teams, Players, n):
    
    Match_Rang_creation(Teams, Players, n)
    
    for j in range(0,n-1):
        h=totes_diferents(Match, n)
        if(h!=1):
            break      
        for i in range(0,n):
            for g in range(0,n):
                if(g==i):
                    continue
                elif(Match[i]==Match[g] and Rang[i]>Rang[g]):
                    Match[i]=Teams[i][j+1]
                    Rang[i]=Rango(Players, n, int(Match[i]), i)
                    break

#With the 'comparar' function it may happen that two Teams pair the same player and one player my be left unpaired (in the last step), this function solves this problem by pairing the most desired player with the better ranked team and the other team goes with the unpaired player.
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
    Teams=crear_matriu_inicial(n)
    print("\n The preference matix for the teams is:")
    print(Teams)
    print("\n The preference matix for the players is:") 
    Players=crear_matriu_inicial(n)
    print(Players)   
    comparar(Teams, Players, n)
    M=ultimes_parelles(contador, Match, Rango, n)
    print("\n The rang vector is: ")
    print(Rang)
    print("\n The Match vector is: ")
    print(M)    
    
main()
