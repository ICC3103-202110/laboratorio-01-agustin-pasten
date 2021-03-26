# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:34:54 2021

@author: Agustin
"""
import random
n = int(input("How many pairs of cards do you want to play? : "))
numero_de_cartas = n*2


lista_n_azar =[]
contador_1 = 0

#In this part,the code create aleatory numbers and put in a list
while contador_1 < numero_de_cartas:
    n_azar = random.randint(1,n)
    
    if lista_n_azar.count(n_azar) == 1:
        lista_n_azar.append(n_azar)
        contador_1 +=1
        
    if lista_n_azar.count(n_azar) == 0:
        lista_n_azar.append(n_azar)
        contador_1 +=1

puntos_j1 = 0
puntos_j2 = 0
print("The points of player1: ",puntos_j1)
print("The points of player2: ",puntos_j2)
print("")
print("")

#In this part, the code create "symbols" of each card
print("the censored cards are:")
for i in range(0,numero_de_cartas):
     print("*")

#In this part, the code create the coordinates of each card
print("the coordinates of each card are: ")

contador_2 = 0
lista_cordenada = []
while contador_2 < numero_de_cartas:
    cordenada =  "(0,"+str(contador_2)+")"
    print(cordenada)
    lista_cordenada.append(cordenada)
    contador_2 +=1


#In this part of the code, begin the part of select diferent cards
lista_cordenada_escogida = []
turnos = 0
while turnos < (n):
        
        desicion_j1  =  input("player1, choose a coordinate shown above, ej: '(x,x)': ")
        for i in range(0,len(lista_cordenada)):
            if i in lista_cordenada_escogida:
                print("")
                continue
            if i != int(desicion_j1[3]):
                print("*")
            if i == int(desicion_j1[3]):
                print(lista_n_azar[int(desicion_j1[3])])
        numero1 =lista_n_azar[int(desicion_j1[3])]
                
          
        desicion2_j1  =  input("player1, choose the second coordinate, ej: '(x,x)': ")
      
        for i in range(0,len(lista_cordenada)):
            
            if i in lista_cordenada_escogida:
                print("")
                continue
            
            if i == int(desicion_j1[3]) :    
                print(lista_n_azar[int(desicion_j1[3])])
                
            if i == int(desicion2_j1[3]) :
                print(lista_n_azar[int(desicion2_j1[3])])
                
            if i != int(desicion2_j1[3]) and i != int(desicion_j1[3]):
                print("*")
        numero2 =lista_n_azar[int(desicion2_j1[3])]


        
        cordenada1_escogida = int(desicion_j1[3])
        lista_cordenada_escogida.append(cordenada1_escogida)    
        cordenada2_escogida = int(desicion2_j1[3])
        lista_cordenada_escogida.append(cordenada2_escogida)
        print(lista_cordenada_escogida)
        
        if numero1 == numero2: 
            puntos_j1 +=1
            print("the player1 has scored a point")
            print("the player1 plays again for reward")
            print("the rest of coordinates are: ")
            for s in range(1,len(lista_n_azar)):
                if s in lista_cordenada_escogida:
                    print("")
                if s not in lista_cordenada_escogida:
                    print("(0,"+str(s)+")")
            turnos +=1 
            if turnos >= n:
                break
            continue
        
        
        print("the rest of coordinates are: ")
        for s in range(1,len(lista_n_azar)):
            if s in lista_cordenada_escogida:
                print("")
            if s not in lista_cordenada_escogida:
                print("(0,"+str(s)+")")
        turnos +=1
        if turnos >= n:
            break
 #here the player2 select some carts
   
        print("")

        
        desicion_j2  =  input("player2, choose a coordinate shown above, ej: '(x,x)': ")
        for i in range(0,len(lista_cordenada)):
            
            if i in lista_cordenada_escogida:
                print("")
                continue
            
            if i != int(desicion_j2[3]):
                print("*")
            if i == int(desicion_j2[3]):
                print(lista_n_azar[int(desicion_j2[3])])
        numero1 =lista_n_azar[int(desicion_j2[3])]
                
                
        desicion2_j2  =  input("player2, choose the second coordinate, ej: '(x,x)': ")
        for i in range(0,len(lista_cordenada)):
            if i in lista_cordenada_escogida:
                print("")
                continue
            
            if i == int(desicion_j2[3]) :    
                print(lista_n_azar[int(desicion_j2[3])])
                
            if i == int(desicion2_j2[3]) :
                print(lista_n_azar[int(desicion2_j2[3])])
                
            if i != int(desicion2_j2[3]) and i != int(desicion_j2[3]):
                print("*")
                
        
        numero2 =lista_n_azar[int(desicion2_j2[3])]
      
 
        cordenada1_escogida = int(desicion_j2[3])
        lista_cordenada_escogida.append(cordenada1_escogida)
        cordenada2_escogida = int(desicion2_j2[3])
        lista_cordenada_escogida.append(cordenada2_escogida)   
        print(lista_cordenada_escogida)
        
        if numero1 == numero2: 
            puntos_j2 +=1
            print("the player2 has scored a point")
            print("the player2 plays again for reward")
            print("the rest of coordinates are: ")
            for s in range(1,len(lista_n_azar)):
                if s in lista_cordenada_escogida:
                    print("")
                if s not in lista_cordenada_escogida:
                    print("(0,"+str(s)+")")
            turnos +=1
            if turnos >=n:
                break
            continue
        

        
        print("the rest of coordinates are: ")
        for s in range(1,len(lista_n_azar)):
            if s in lista_cordenada_escogida:
                print("")
            if s not in lista_cordenada_escogida:
                print("(0,"+str(s)+")")
        turnos +=1
        if turnos >= n:
            break
    
if puntos_j1 > puntos_j2:
    print("the winner is the player1 with",puntos_j1,"points, while the player2 has",puntos_j2,"points")

if puntos_j1 < puntos_j2:
    print("the winner is the player2 with",puntos_j2,"points, while the player1 has",puntos_j1,"points")

if puntos_j1 == puntos_j2:
    print("It´s a tie, because the players 1 and 2 has the same points, wich is:",puntos_j1)

print("The game it's over")

    