d1={}
for i in range(int(input())):
    data=input().split(': ')
    d1[data[0]]=set(data[1].split(', '))
check=input().strip()
c=0
for e in d1:
    set1=d1[check]&d1[e]
    if check==e:
        continue
    if len(set1)>0:
        print(e)
        c=1
if c==0:
    print('Not Found')
    