import math

c = str(input().strip())
if not c == 'S':
    if c == 'R':
        n = int(input().strip())
        sum_n = 0
        k=0
        for i in range(n+1):
            sum_n += ((-3)**(-k)) / (2*k+1)
            k+=1
        p = math.sqrt(12)*sum_n
        p = round(p,12)
        print('pi =',p)
    else:
        if c == 'P':
             p=math.sqrt(7+math.sqrt(6+math.sqrt(5)))
             p=round(p,6)
             print('pi =',p)
        else:
             print('Invalid')
else:
    m = int(input().strip())
    q,r,t,k,n,x,i,p = 1,0,1,1,3,3,0,''
    while True:
        if i<m:
            if 4*q+r-t<n*t:
                p=p+str(n)
                i=i+1
                a=10*(r-n*t)
                n=10*(3*q+r)//t-10*n
                q=10*q
                r=a
            else:
                a=(2*q+r)*x
                b=(7*q*k+2+x*r)//(x*t)
                q=k*q
                t=x*t
                x=x+2
                k=k+1
                n=b
                r=a
        else:
            break
    p=p[0]+'.'+p[1:]
    print('pi =',p)
            
