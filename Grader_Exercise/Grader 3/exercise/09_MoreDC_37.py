d1={}
for i in range(int(input())):
    data=input().split()
    d1[data[0]]=int(data[1])
l1=[]
for i in range(int(input())):
    l1.append(input().split())
l1=sorted(sorted(l1),key=lambda a:-float(a[1]))

def check(d1,p1):
    for i in range(2,6):
        if d1[p1[i]]!=0:
            d1[p1[i]]-=1
            return [p1[0],p1[i]]
l2=[]
for i in range(len(l1)):
    l2.append(check(d1,l1[i]))
  
[print(f"{e[0]} {e[1]}") for e in sorted(l2)]
