import math

a=float(input())
def bisection(a):
    L=0
    U=a

    while True:
        x=(L+U)/2
        if abs(a-10**x)<=1e-10*max(a,10**x):
            return round(x,6)
        if 10**x > a:
            U = x
        if 10**x < a:
            L = x
    
print(bisection(a))