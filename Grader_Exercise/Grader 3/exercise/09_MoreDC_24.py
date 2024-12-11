d1={}
while True:
    data=input().strip()
    if data=='q':
        break
    name,genr=data.split(', ')
    if genr not in d1:
        d1[genr]=[name]
    else:
        d1[genr].append(name)

# l1=sorted(d1.items(),key=lambda a:-len(a[1]))
l1=list(d1.items())
for i in range(len(l1)):
    print(f'{l1[i][0]}: {", ".join(l1[i][1])}')
