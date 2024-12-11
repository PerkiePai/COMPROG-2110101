def f1(a,b,c):
    x = [a,b,c]
    x.sort()
    if x[1] > 0:
        return x[1]
    else :
        return x[2]
        
def f2(a,b,c):
    if a>0:
        if b>c and b<0:
            return b
        elif c<0:
            return c
    elif b>0:
        if a>c and a<0:
            return a
        elif c<0:
            return c
    elif c>0:
        if a>b and a<0:
            return a
        elif b<0:
            return b
    
def f3(a,b,c):
    sum = str(a+b+c)
    if sum[0]=='-':
        return sum[1]
    return sum[0]
    
def f4(a,b,c):
    sum = str(a+b+c)
    return sum[-1]
    
def main():
    s1,s2,a,b,c = [int(e) for e in input().split()]
    if s1==0 and s2==0:
        print(f1(a,b,c))
    elif s1==0 and s2==1:
        print(f2(a,b,c))
    elif s1==1 and s2==0:
        print(f3(a,b,c))
    elif s1==1 and s2==1:
        print(f4(a,b,c))
    else:
        print('Error')
    
    
exec(input().strip())