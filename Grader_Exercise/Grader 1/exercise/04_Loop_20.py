a = input().split()

x=0
y=1
x_max=int(a[x])
x_min=int(a[x])
y_max=int(a[y])
y_min=int(a[y])

line=1

def is_number(s):
    try:
        float(s)  # Try converting to float
        return True
    except ValueError:
        return False
    
while is_number(a[0]):
    if x_max<int(a[x]):
        x_max=int(a[x])
    if x_min>int(a[x]):
        x_min=int(a[x])
    if y_max<int(a[y]):
        y_max=int(a[y])
    if y_min>int(a[y]):
        y_min=int(a[y])
    a = input().split()
    x,y=y,x
    line+=1
    
if line%2==0:
    x,y=y,x

mode = a[0]
if mode == 'Zig-Zag':
    print(x_min,y_max)
elif mode == 'Zag-Zig':
    print(y_min,x_max)
else:
    print('Error')
    

