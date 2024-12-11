d1={}
for i in range(int(input())):
    data=[e for e in input().split(', ')]
    time=int(data[3].split(':')[0])*60+int(data[3].split(':')[1])
    genr=data[2]
    if genr not in d1:
        d1[genr]=time
    else:
        d1[genr]+=time

l1=sorted([e for e in d1.items()], key=lambda a:-a[1])
for i in range(len(l1[:3])):
    sec='0'+str(l1[i][1]%60)
    print(f'{l1[i][0]} --> {l1[i][1]//60}:{sec[-2:]}')

