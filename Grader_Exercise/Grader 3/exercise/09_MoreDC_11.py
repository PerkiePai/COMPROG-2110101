n = int(input().strip())

output = []
for i in range(n):
    line = input()
    if line[:1] == '.':
        count = 0
        for j in range(0,len(line),2):
            if line[j] == '.':
                count += 1
            else:
                break
        output.append('.'*count + line[count*2:])
    else:
        output.append(line)

for i in output:
    print(i)
