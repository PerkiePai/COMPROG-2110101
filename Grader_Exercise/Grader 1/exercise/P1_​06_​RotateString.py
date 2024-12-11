operator = input()
n = int(input())
lines = [input().strip() for _ in range(n)]
string=''

def check_lenght():
    for i in range(n):
        if len(lines[0]) != len(lines[i]):
            print('Invalid size')
            return False
    return True
    
for i in range(n):
    string+=lines[i]


if check_lenght()==True:    
    if operator == '90':
        output=''
        for i in range((n-1)*len(lines[0]),(n-1)*len(lines[0])+len(lines[0]),1):
            for j in range(i,-1,-len(lines[0])):
                output+=string[j]
            print(output)
            output=''
    elif operator == 'flip':
        output=''
        for i in range(len(lines[0])-1,len(lines[0])*n,len(lines[0])):
            for j in range(i,i-len(lines[0]),-1):
                output+=string[j]
            print(output)
            output=''
    elif operator == '180':
        output=''
        for i in range(len(lines[0])*n-1,-1,-len(lines[0])):
            for j in range(i,i-len(lines[0]),-1):
                output+=string[j]
            print(output)
            output=''
    


    
    