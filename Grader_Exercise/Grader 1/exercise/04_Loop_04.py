string = input()
output = ''


for i in range(len(string)):
    if string[i] == '(':
        output+='['
    elif string[i] == ')':
        output+=']'
    elif string[i] == '[':
        output+='('
    elif string[i] == ']':
        output+=')'
    else:
        output+=string[i]
print(output)
