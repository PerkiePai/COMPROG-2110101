q1=[]
q2=[]
q3=[]
q=0

for i in range(int(input())):
    c=input().split()
    if c[0] == 'reset':
        n=int(c[1])
        q1.append(n-1)
        q2.append(0)
        q3.append(0)
        
    elif c[0] == 'new':
        n=int(c[1])
        q1.append(q1[-1]+1)
        q2.append(n)
        print(f'ticket {q1[-1]}')
        
    elif c[0] == 'next':
        q+=1
        print(f'call {q1[q]}')
        
        
    elif c[0] == 'order':
        n=int(c[1])
        print(f'qtime {q1[q]} {n-q2[q]}')
        q3.append(n-q2[q])
    
    elif c[0] == 'avg_qtime':
        print(f'avg_qtime {sum(q3)/(len(q3)-1)}')
    
    
