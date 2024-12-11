def pattern1(nrows, ncols):
    l1=[]
    for i in range(nrows):
        l2=[]
        for j in range(i*ncols+1,(i+1)*ncols+1):
            l2.append(j)
        l1.append(l2)
    return l1

def pattern2(nrows,ncols):
    l1=[]
    for i in range(1,nrows+1):
        l2=[]
        for j in range(i,i+nrows*ncols,nrows):
            l2.append(j)
        l1.append(l2)
    return l1

def pattern3(N):
    l1=[]
    cnt=1
    for i in range(N):
        l2=[]
        for j in range(i):
            l2.append(0)
        for j in range(N-i):
            l2.append(cnt)
            cnt+=1
        l1.append(l2)
    return l1
            
def pattern4(N):
    l1=[]
    cnt=1
    for i in range(1,N+1):
        for j in range(N-i):
            l1.append(0)
        for j in range(i):
            l1.append(cnt)
            cnt+=1
            
    out=[]
    for i in range(N-1,-1,-1):
        l2=[]
        for j in range(i,N**2+i,N):
            l2.append(l1[j])
        out.append(l2)
    return out
            
def pattern5(N):
    l1=[]
    for i in range(N):
        l2=[]
        cnt=N
        for j in range(i):
            l2.append(0)
        for j in range(N-i):
            l2.append(i+1)
            i+=cnt
            cnt-=1
        l1.append(l2)
    return l1

def pattern6(N):
    l1=[[] for i in range(N)]
    for i in range(N):
        for j in range(N-i-1):
            l1[i].append(0)

    row=0
    cnt=1
    
    max_cnt=0
    for i in range(N+1):
        max_cnt+=i
        
    while cnt<max_cnt+1:
        start=row
        while row<N:
            l1[row].append(cnt) 
            row+=1
            cnt+=1
        row-=1
        while row>start:
            l1[row].append(cnt)
            row-=1
            cnt+=1
        row+=2
        
    out=[]
    for i in range(N-1,-1,-1):
        l2=[]
        for j in range(N):
            l2.append(l1[j].pop(-1))
        out.append(l2)
        
    return out
        
exec(input().strip())




