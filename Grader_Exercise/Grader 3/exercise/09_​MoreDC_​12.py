u1=set()
i1=set()

for i in range(int(input())):
    data=set([int(e) for e in input().strip().split()])
    if i==0:
        u1=data
        i1=data
    else:
        u1 = u1|data
        i1 = i1&data

print(len(u1))
print(len(i1))