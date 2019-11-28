# Stable_Marrige
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
    

def comparar(Boys, Girls, n):
    
    Match_Rang_creation(Boys, Girls, n)
    
    for j in range(0,n-1):
        for i in range(0,n):
            r=i+1
            for g in range(r,n):
                if(Match[i]==Match[g]):
                    if(Rang[i]<Rang[g]):
                        Match1[g]=Boys[i][j+1]
                    else:
                        Match1[i]=Boys[i][j+1]
                else:
                    Match1[i]=Match[i]
        if(totes diferents):
            break;
                    
def main():
    Boys=crear_matriu_inicial(n)
    Girls=crear_matriu_inicial(n)
    #print(Boys)
    #print(Girls)
    
    comparar(Boys, Girls, n)
    print(Rang)
    print(Match)
main()

