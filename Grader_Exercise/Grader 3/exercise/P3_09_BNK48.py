from icecream import ic

d1={}
d2={}
d3={}
while True:
    data=input().strip().split()
    if len(data)==1:
        break
    ota,idol,point=data[0],data[1],int(data[2])

    #1
    if idol in d1:
        d1[idol]+=point
    else:
        d1[idol]=point

    #2
    if idol in d2:
        d2[idol]=d2[idol]|{ota}
    else:
        d2[idol]={ota}

    #3
    if ota in d3:
        if idol in d3[ota]:
            d3[ota][idol]+=point
        else:
            d3[ota][idol]=point
    else:
        d3[ota]={idol:point}
ic(d1,d2,d3)


if data==['1']:
    l1=sorted([e for e in d1.items()],key=lambda a:-a[1])[:3]
    [print(', '.join([e[0] for e in l1]))]
elif data==['2']:
    l2=[]
    for k,v in d2.items():
        l2.append([k,len(v)])
    l2=sorted(l2,key=lambda a:-a[1])[:3]
    [print(', '.join([e[0] for e in l2]))]
elif data==['3']:
    d33={}
    for k,v in d1.items():
        d33[k]=0
    for k,v in d3.items():
        bestidol=sorted(sorted(d3[k].items()),key=lambda a:-a[1])[0][0]
        if bestidol in d33:
            d33[bestidol]+=1
        else:
            d33[bestidol]=1

    l3=sorted(d33.items(),key=lambda a:-a[1])[:3]
    [print(', '.join([e[0] for e in l3]).strip())]