# fname=input()
fname='Year1/data/101.txt'
with open(fname,'r') as f:
    l1=[]
    for line1 in f:
        l1.append(line1.strip())

    l2=[]
    for i in range(len(l1[0])):
        line=''
        for e in l1:
            line+=e[i]
        l2.append(line)

def p(l2):
    for i in range(len(l2[0])):
        line=''
        for e in l2:
            line+=e[i]
        print(line)

check=input()
if check=='LSTRIP':
    l3=[e for e in l2]
    for e in l3:
        if e=='.'*len(l2[0]):
            l2.remove(e)
        else:
            break
    p(l2)

elif check=='RSTRIP':
    l1=l2[::-1]
    l3=[e for e in l1]
    for e in l3:
        if e=='.'*len(l1[0]):
            l1.remove(e)
        else:
            l2=l1[::-1]
            break
    p(l2)

elif check=='STRIP':
    l3=[e for e in l2]
    for e in l3:
        if e=='.'*len(l2[0]):
            l2.remove(e)
        else:
            break

    l1=l2[::-1]
    l3=[e for e in l1]
    for e in l3:
        if e=='.'*len(l1[0]):
            l1.remove(e)
        else:
            l2=l1[::-1]
            break
    p(l2)

elif check=='STRIP_ALL':
    l3=[e for e in l2]
    for e in l3:
        if e=='.'*len(l2[0]):
            l2.remove(e)
    p(l2)

else:
    print("Invalid command")
