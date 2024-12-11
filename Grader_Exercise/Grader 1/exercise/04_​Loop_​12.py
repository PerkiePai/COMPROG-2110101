line = int(input())

x=[]
y=[]
for _ in range(line):
    a =  input().split()
    x.append(int(a[0]))
    y.append(int(a[1]))
    x,y=y,x
    
if line%2==0:
    x,y=y,x

mode = input().strip()
if mode == 'Zig-Zag':
    print(min(y),max(x))
elif mode == 'Zag-Zig':
    print(min(x),max(y))
else:
    print('Error')
    
