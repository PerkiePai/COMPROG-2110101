d1,d2,d3={},{},{}


for i in range(int(input())):
    data=input().strip().split()
    if data[0]=='B':
        buyer,product,price=data[1],data[2],int(data[3])
        if product in d1:
            d1[product][buyer]=price
        else:
            d1[product]={buyer:price}
    elif data[0]=='W':
        buyer,product=data[1],data[2]
        if product in d1:
            if buyer in d1[product]:
                d1[product][buyer]=0

    if buyer not in d2:
        d2[buyer]=0
    if buyer not in d3:
        d3[buyer]=[]

# print(d1,end='\n')
# print(d2,end='\n')
# print(d3,end='\n')
# print()
l1=[[k1,v1] for k in d1.keys() for k1,v1 in d1[k].items() if v1!=0]
print(l1)
for k,v in d1.items():
    bestprice=sorted([[k1,v1] for k1,v1 in d1[k].items() if v1!=0],key=lambda a:-a[1])[0]
    buyer,price=bestprice[0],bestprice[1]
    d2[buyer]+=price
    d3[buyer].append(k)

# print(d1,end='\n')
# print(d2,end='\n')
# print(d3,end='\n')
l1=[]
for k,v in d2.items():
    # if d3[k]!=[]:
    #     print(f"{k}: ${d2[k]} -> {' '.join(sorted(d3[k]))}")
    # else: 
    #     print(f"{k}: ${d2[k]}")
    l1.append([k,d2[k],sorted(d3[k])])
l1=sorted(l1)

for e in l1:
    if e[2]!=[]:
        print(f"{e[0]}: ${e[1]} -> {' '.join(e[2])}")
    else: 
        print(f"{e[0]}: ${e[1]}")