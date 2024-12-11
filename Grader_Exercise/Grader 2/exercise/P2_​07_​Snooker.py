dict1={'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7,'':0,'X':0}
s1=0
s2=0
n=0
def score(t):
    return dict1[t[1:2]]+dict1[t[2:3]]
        
while True:
    if n==18:
        break
    t=input()
    if t[0]=='1':
        s1+=score(t)
    elif t[0]=='2':
        s2+=score(t)
    if len(t)==2:
        if t[1:2]!='X':
            n+=1
    elif len(t)==3:
        if t[1:2]=='X':
            n+=1
        else:
            n+=2
            
print(s1,s2)
if s1>s2:
    print('Player 1 wins')
elif s2>s1:
    print('Player 2 wins')
else:
    print('Tie')
        
