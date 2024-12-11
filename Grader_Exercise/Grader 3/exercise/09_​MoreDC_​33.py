def L2D(l1):
    return dict(zip([e[1] for e in l1],[e[0] for e in l1]))

def D2L(d1):
    return [(v,k) for k,v in d1.items()]

def Lno0(l1):
    return [e for e in l1 if e[0]!=0]

def add_poly(p1, p2):
    if len(p1)<len(p2):
        p1,p2=p2,p1

    d1=L2D(p1)
    d2=L2D(p2)

    for m in d2:
        if m in d1:
            d1[m]+=d2[m]
        else:
            d1[m]=d2[m]
    l1=D2L(d1)
    l1=sorted(Lno0(l1),key=lambda a:-a[1])
    return l1
    
def mult_poly(p1, p2):
    if len(p1)<len(p2):
        p1,p2=p2,p1
    b=[]
    for m in p2:
        b1=[]
        for n in p1:
            b1.append((m[0]*n[0],m[1]+n[1]))
        b.append(b1)
    base=[]
    while len(b)>0:
        base=b.pop(0)
        if len(b)==0:
            base=add_poly(base, b.pop(0))
            break
        base=add_poly(base, b.pop(0))
    return base
    
for i in range(3):
    exec(input().strip())