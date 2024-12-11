def spiral_square(n):
    l1=[[0 for i in range(n)] for j in range(n)]
    # print(l1)
    x,y=n//2,n//2
    cnt=1
    rnd=1
    l1[y][x]=cnt
    cnt+=1
    x+=1
    while cnt<=n**2:
        for i in range(rnd): #up
            l1[y][x]=cnt
            cnt+=1
            y-=1
        for i in range(rnd): #left
            l1[y][x]=cnt
            cnt+=1
            x-=1
        rnd+=1
        l1[y][x]=cnt
        cnt+=1
        x-=1
        for i in range(rnd): #down
            l1[y][x]=cnt
            cnt+=1
            y+=1
        for i in range(rnd): #right
            l1[y][x]=cnt
            cnt+=1
            x+=1
        l1[y][x]=cnt
        cnt+=1
        x+=1
        rnd+=1
        
    return l1

def print_square(l1):
    return [print(' '.join(map(str,e))) for e in l1]

exec(input().strip())