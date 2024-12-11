def T2S(c):
    l1=['A','E','I','L','N','O','R','S','T','U']
    if c in l1:
        return 1
    l1=['D','G']
    if c in l1:
        return 2
    l1=['B','C','M','P']
    if c in l1:
        return 3
    l1=['F','H','V','W','Y']
    if c in l1:
        return 4
    l1=['K']
    if c in l1:
        return 5
    l1=['J','X']
    if c in l1:
        return 8
    l1=['Q','Z']
    if c in l1:
        return 10

t=[e for e in input().strip().upper().split()]
l1=[]
for word in t:
    s=0
    for char in word:
        s+=T2S(char)
    l1.append([s,word])
l1=sorted(l1, key=lambda a:-a[0])
for i in range(len(l1)):
    print(l1[i][1],l1[i][0])
    