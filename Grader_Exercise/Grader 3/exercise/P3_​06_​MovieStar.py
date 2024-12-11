d1={}
for i in range(int(input())):
    data=input().split(', ')
    if data[1] in d1:
        d1[data[1]].append(data[0])
    else:
        d1[data[1]]=[data[0]]
    if data[2] in d1:
        d1[data[2]].append(data[0])
    else:
        d1[data[2]]=[data[0]]

    
check = input().strip().split(', ')
for e in check:
    if e in d1:
        print(f"{e} -> {', '.join(d1[e])}")
    else:
        print(f"{e} -> {'Not found'}")
