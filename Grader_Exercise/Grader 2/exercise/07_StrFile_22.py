lowercase = "abcdefghijklmnopqrstuvwxyz"
l1 = 'nopqrstuvwxyzabcdefghijklm'
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
u1 = 'NOPQRSTUVWXYZABCDEFGHIJKLM'

while True:
    line = input().strip()
    if line == 'end':
        break
    else:
        output = ''
        for i in range(len(line)):
            if line[i] in lowercase:
                output+=l1[lowercase.index(line[i])]
            elif line[i] in uppercase:
                output+=u1[uppercase.index(line[i])]
            else:
                output+=line[i]
        print(output)
        