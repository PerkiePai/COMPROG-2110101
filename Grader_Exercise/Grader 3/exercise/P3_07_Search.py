def count(word,s1):
    c=0
    for e in s1:
        if word==e:
            c+=1
    return c

def updateScore(word,d2,d3):
    for e in d1:
        d1[e]+=(count(word,d2[e])/len(d2[e]))*(1/len(d3[e]))
    return

d1={}
d2={}
for i in range(int(input())):
    fname=input().strip()
    doc=input().strip().split()
    d1[fname]=0
    d2[fname]=doc
d3={}
for e in d2:
    s1=set()
    for e1 in d2[e]:
        if e1 not in s1:
            s1.add(e1)
    d3[e]=s1

while True:
    data=input()
    if data=='-1':
        break
    updateScore(data,d2,d3)
    best=sorted(list(d1.items()),key=lambda a:-a[1])[0]
    if best[1]!=0:
        print(best[0])
    else:
        print('NOT FOUND')
    for e in d1:
        d1[e]=0
    