i,ii,iii = [int(e) for e in input().split()]
d1={}
for i in range(i):
    data=input().split()
    d1[data[0]]=data[1]


d2={}
for i in range(ii):
    data=input().split()
    for j in range(1,len(data)):
        if data[0] in d2:
            d2[data[0]]=d2[data[0]]|{d1[data[j]]}
        else:
            d2[data[0]]={d1[data[j]]}

for i in range(iii):
    data=input().split()
    un=d2[data[0]]
    for j in range(1,len(data)):
        un=un&d2[data[j]]
    if len(un)==0:
        print('None')
    else:
        print(' '.join(un))

