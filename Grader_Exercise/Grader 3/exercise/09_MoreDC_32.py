def first_fit(L, e):
    if L==[]:
        L.append([e])
        return L
    for l in L:
        if sum(l)+e<=100:
            l.append(e)
            return L
    L.append([e])
    return L

def best_fit(L, e):
    check=[]
    if L==[]:
        L.append([e])
        return L
    for l in L:
        if sum(l)+e<=100:
            check.append(sum(l)+e)
        else:
            check.append(-1)
    if max(check)==-1:
        L.append([e])
        return L
    L[check.index(max(check))].append(e)
    return L     
        
def partition_FF(D):
    L1=[]
    for num in D:
        L1=first_fit(L1, num)
    return L1

def partition_BF(D):
    L1=[]
    for num in D:
        L1=best_fit(L1, num)
    return L1

exec(input().strip()) 