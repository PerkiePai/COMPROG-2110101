n,a,b = [int(e) for e in input().split()]

if a>b:
    d,e = -1,-1
    while True:
        if n<a:
            c = int(input())
            if c>d:
                d,e=c,d
            else:
                if c>e:
                    e=c
            n=n+b
        else:
            break
else:
    c,d,e,f = [int(input()) for _ in range(4)]
    if e<f:
        e,f=f,e
    if d<e:
        d,e=e,d
    if c<d:
        c,d=d,c
    if d>e:
        if not d>f:
            d,f=f,d
    else:
        if e>f:
            d,e=e,d
        else:
            d,f=f,d

print(d,e)
        