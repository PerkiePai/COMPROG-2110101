string = input()

num = ['0','1','2','3','4','5','6','7','8','9']

atleast = 0
found = 0

output = ''
for i in range(10):
    for j in range(len(string)):
        if string[j] == num[i]:
            found = 1
            atleast = 1
    if found == 0:
        output += ','+num[i]
    found = 0
    
if atleast == 0:
    print('0,1,2,3,4,5,6,7,8,9')
elif output == '':
    print('None')
else:
    print(output[1:])
    
    