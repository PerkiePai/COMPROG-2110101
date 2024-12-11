N=int(input())
d1={}
for i in range(N):
    line=input().strip().split()
    d1[line[0]+' '+line[1]]=line[2]
d2=dict(zip(d1.values(),d1.keys()))
M=int(input())
for i in range(M):
    ask=input().strip()
    if ask in d1:
        print(f'{ask} --> {d1[ask]}')
    elif ask in d2:
        print(f'{ask} --> {d2[ask]}')
    else:
        print(f'{ask} --> Not found')
