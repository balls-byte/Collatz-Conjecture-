import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def calcColatch(n:int,counter=0,liste=None):
    if liste is None:
        liste=[n]

    
    counter=counter+1
    if n!=1:
        if n%2==0:
            newN=n/2
            print(newN)
            liste.append(newN)
            
        else:
            newN=3*n+1
            print(newN)
            liste.append(newN)
            
        return calcColatch(newN,counter,liste)
    else:
        print("Counter: ",counter) 
        return liste

def calcColatchSim(n:int):
    if n%2==0:
            print(n/2)
            liste.append(n/2)
            calcColatch(n/2)
    else:
        print(3*n+1)
        liste.append(3*n+1)
        calcColatch(3*n+1)
start=8
plot=calcColatch(start)
fig=plt.figure()
axis=plt.axes(xlim=(0,len(plot)),ylim=(0, max(plot)+10))
title="Startzahl: ",start
plt.title(title)
line,=axis.plot([],[],lw=3)
def init():
     line.set_data([],[])
     return line,
def animate(i):
     x=list(range(i+1))
     y=plot[:i+1]
     line.set_data(x,y)
     return line,
#anim=FuncAnimation(fig, animate, init_func=init, frames=len(plot), interval=400, blit=True)
#anim.save("CollatzConjecture27.gif",writer="pillow",fps=2)
plt.plot(plot)
plt.figtext(start)
plt.show()
