a,b,c,d = [int(e) for e in input().split()]

if a>b:
    a,b = b,a
    while True:
        if not d>=a:
            break
        else:
            if c>d:
                a+=1
            else:
                d-=1
else:
    if c%2==0:
        d=d+a
    else:
        if d>c:
            c=c+d
        else:
            b=b+c
        a=b+c
print(a,b,c,d)
            
        