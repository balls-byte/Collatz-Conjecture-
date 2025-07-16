import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from termcolor import colored, cprint

def calcCollatz(n: int, counter=0, liste=None):
    if liste is None:
        liste = [n]

    counter = counter + 1
    if n != 1:
        if n % 2 == 0:
            newN = n // 2
            liste.append(newN)
        else:
            newN = 3 * n + 1
            liste.append(newN)

        return calcCollatz(newN, counter, liste)
    else:
        print("Counter:", counter)
        return liste
    
col=8 # Die 4 ändern um mehr Glieder zu berechnen
end =17 #Hier ändern um mehr Startwerte zu berechnen
def calcCollatzEdit(n: int, counter=0, liste=None):
    if liste is None:
        liste = [n]

    counter = counter + 1

    if counter <= col:
        if n % 2 == 0:
            newN = n // 2
            liste.append(newN)
        else:
            newN = (3 * n + 1)/2
            liste.append(newN)

        return calcCollatzEdit(newN, counter, liste)
    else:
        return liste

matrix = []
for i in range(1, end):
    print("Startwert", i)
    rows = []
    rows.append(i)
    rows.append(calcCollatzEdit(i))
    matrix.append(rows)


for i in range(len(matrix)):
    for j in range(len(matrix[i][1])):
        if j <= col:  
            if matrix[i][1][j] % 2 == 0:
                print(colored(f"{matrix[i][1][j]} ","green"))
            else:
                print(colored(f"{matrix[i][1][j]} ","red"))
    print()
