def row_number(t, e):
    cnt=0
    for subl in t:
        for char in subl:
            if char == e:
                return cnt    
        cnt+=1
        
def flatten(t):
    l1 = [e for a in t for e in a if e!=0]
    return l1

def inversions(x):
    cnt=0
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i]>x[j]:
                cnt+=1
    return cnt

def solvable(t):
    t1=flatten(t)
    if len(t)%2!=0:
        if inversions(t1)%2==0:
            return True
    else:
        if inversions(t1)%2==0:
            if row_number(t, 0)%2!=0:
                return True
        else:
            if row_number(t, 0)%2==0:
                return True
    return False
                
        
exec(input().strip())

        
            