w1=[]
l1=[]
for i in range(int(input())):
    data = [e for e in input().split()]
    w1.append(data[0])
    l1.append(data[1])

w1=set(w1)
l1=set(l1)
allwin = w1 - (w1 & l1)

print(sorted(allwin))