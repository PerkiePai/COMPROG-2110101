d1={}
while True:
    data=input().split()
    if len(data)==1:
        data=data[0]
        break
    if data[0] in d1:
        d1[data[0]].append(data[1])
    else:
        d1[data[0]]=[data[1]]
    if data[1] in d1:
        d1[data[1]].append(data[0])
    else:
        d1[data[1]]=[data[0]]
if data not in d1:
    d1[data]={data}
baseSet=set(d1[data])
for e in d1[data]:
    baseSet=baseSet|set(d1[e])

[print(e) for e in sorted(baseSet)]