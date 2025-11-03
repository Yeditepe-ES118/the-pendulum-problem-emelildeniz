
import  math 
def find_period(L0:int, L1:int):   
   #LO,L1: integers, with L1 > L0 > 0
   #Formula: T=2*pi*sqrt(L/g)
    g=9.81 # in m/s^2 
    T0= None
    T1= None
    for L in range(L0, L1+1):
        T= 2 * math.pi * math.sqrt(L / g)
        print (f"When L = {L:4.1f} m, T = {T:.1f} s")
        if L==L0:
           T0=T
        if L==L1:
           T1=T
    return T0, T1

    

    