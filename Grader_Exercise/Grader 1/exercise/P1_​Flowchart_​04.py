x1 = input().strip()
x2 = input().strip()
x3 = input().strip()

x=x1+x2+x3
if not len(x) == 9:
    print('ERROR')
else:
    win = '-'
    i=0
    while True:
        if i<3:
            if x[3*i] == x[3*i+1] and x[3*i] == x[3*i+2] and x[3*i+1] == x[3*i+2]:
                win = x[3*i]
                break
            if x[i] == x[i+3] and x[i] == x[i+6] and x[i+3] == x[i+6]:
                win = x[i]
                break
            i+=1
        else:
            break
    if win == '-':
        if x[0] == x[4] and x[0] == x[8] and x[4]== x[8]:
            win = x[0]
        if x[3] == x[4] and x[3] == x[6] and x[4]== x[6]:
            win = x[6]
    if win == '-':
        print('???')
    else:
        print(win)
        
