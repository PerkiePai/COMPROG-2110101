import math

def sqrt_n_times(x, n):
    for i in range(n):
        x=math.sqrt(x)
    return x

def cube_root(y):
    y=sqrt_n_times(y,2)
    n=2
    while n<=32:
        y*=sqrt_n_times(y,n)
        n*=2
    return y
        
def main():
    q = float(input())
    print(cube_root(q))
    
exec(input()) # DON'T remove this line