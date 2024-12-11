fname='Year1/data/data2.txt'
k=10
with open(fname,'r') as f:
    ruler=''
    for i in range(1,k+1):
        if i%10!=0:
            ruler+='-'
        else:
            ruler+=str(i//10)
    print(ruler)
    doc=''
    for e in f.readlines():
        doc+=e.replace("\n",".")
    doc=doc.strip('.')+'.'
    
l1=[]
idx=0
for i in range(1,len(doc)):
    if doc[i-1]!='.' and doc[i]=='.':
        l1.append(doc[idx:i])
        idx=i

c=0
for i in range(len(l1)):
    c+=len(l1[i])
    if c>k:
        l1[i]='\n'+l1[i].strip('.')
        c=len(l1[i])-1
        
[print(e,end='') for e in l1]