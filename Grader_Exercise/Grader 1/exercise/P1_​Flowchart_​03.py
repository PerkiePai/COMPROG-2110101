import math

a,b,c,d = [int(e) for e in input().split()]

if a==1:
    c,d = d,c
    if not b==1:
        if not b==2:
            if b!=3:
                c=c+c**d
            else:
                c=c/d
        else:
            c=c-d
    else:
       c=c+d
    a = (d+math.sqrt(((c/b)**3)+d)) / (2+b*d)
    
else:
    if a==2:
        if b>1:
            c=c+d
        if b>2:
            c=c/d
        if b>3:
            c=c+c**d
        else:
            a=math.log(c,10)
    else:
        while a>d:
            a=a-2
            if not a<b:
                c=c+a
            else:
                break
                
print(a,b,c,d)