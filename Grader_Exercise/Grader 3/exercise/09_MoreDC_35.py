l1=[]
for i in range(int(input())):
    data=input().split()
    name,grade,score,major=data[0],data[1],data[2],data[3]
    l1.append([name,grade,score,major])
check=input().split()
l2=[[e[0],e[1: ]] for e in l1]
for i in range(len(check)):
    l2=[e for e in l2 if check[i] in e[1]]
if l2==[]:
    print('Not Found')
else:
    l2=sorted(l2,key=lambda a:a[0])
    for e in l2:
        print(f'{e[0]} {" ".join(e[1])}')
        
