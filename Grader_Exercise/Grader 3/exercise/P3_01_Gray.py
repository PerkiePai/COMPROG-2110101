def check(n,k):
    isValid=True
    if (n<0 or n%1!=0) and (k<0 or k%1!=0):
        print('Invalid n and k')
        isValid=False
    elif (n<0 or n%1!=0):
        print('Invalid n')
        isValid=False
    elif (k<0 or k%1!=0):
        print('Invalid k')
        isValid=False
    return isValid

l1=[str(0),str(1)]
def gayCode(l1):
    l2=l1[::-1]
    l1=['0'+e for e in l1]
    l2=['1'+e for e in l2]
    return l1+l2

n,k=int(input()),int(input())

if check(n,k):
    firstLine=''
    for i in range(1,k+1):
        firstLine+='-'+str(i)+'-'*(n-len(str(i)))
    print(firstLine[1:])
    for i in range(n-1):
        l1=gayCode(l1)
    for i in range((len(l1)-1)//k+1):
        l2=[l1.pop(0) for e in range(k) if l1!=[]]
        print(','.join(l2))
        
        
