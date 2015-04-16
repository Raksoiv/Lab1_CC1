from math import *

def Mavillan ():
    for i in range(1,21):
        a = 10**(-i)
        b = (1-(1/cos(a)))/((tan(a)**2))
        print(b)
    print ("\n")
    
Mavillan()