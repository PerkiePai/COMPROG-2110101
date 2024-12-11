l1=[]
for i in range(int(input())):
    line = input().strip().split()
    l1.append(line)
line = input().strip().split()

if line[0] == 'show':
    for i in range(len(l1)):
        print(" ".join(l1[i]))

if line[0] == 'get':
    if line[1] in [e[0] for e in l1]:
        idx=[e[0] for e in l1].index(line[1])
        print(' '.join(l1[idx]))
    else:
        print(f'{line[1]} not found')

if line[0] == 'avg':
    i=int(line[1])
    l2=[]
    for e in l1:
        l2.append(float(e[i]))
    print(round(sum(l2)/len(l2),4)) 

if line[0] == 'max':
    i=int(line[1])
    l1.sort()
    l2=[]
    for e in l1:
        l2.append(float(e[i]))
    idx=l2.index(max(l2))
    print(l1[idx][0],l1[idx][i])

if line[0] == 'sort':
    i=int(line[1])
    l2=[]
    for e in l1:
        l2.append([e[0],float(e[i])])
    l2 = sorted(l2,key=lambda a:a[0])
    l2 = sorted(l2,key=lambda a:a[1])
    l3 = [e[0] for e in l2]
    print(' '.join(l3))
    
    
    