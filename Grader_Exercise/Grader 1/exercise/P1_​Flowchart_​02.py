n,k = [int(e) for e in input().split()]

if n%2==1:
    sum_a, sum_b, sum_c, m = 0,0,0,0
    while True:
        if m<k:
            a,b,c = [int(e) for e in input().split()]
            if a==b:
                if a==b and a==c and b==c:
                    if not a+b>k:
                        sum_a-=3
                        sum_b-=2
                        sum_c+=1
                    else:
                        sum_a+=1
                        sum_b+=2
                        sum_c-=3
                else:
                    sum_a+=2
                    sum_b-=3
            m+=1
        else:
            print(sum_a,sum_b,sum_c)
            break
        
else:
    s,t = [int(e) for e in input().split()]
    x,y = s,t
    if not s>t:
        if s<t:
           y = 2*(t-s) 
    else:
        x = s-t
    if x+y>k:
        x,y = y,x
        x=y+s**2
        
    print(x,y)
        
    