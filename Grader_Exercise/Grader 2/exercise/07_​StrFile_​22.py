n=2
data = ["" for j in range(n)]
for i in range(n):
    data[i] = sorted(list(input().strip().lower().replace(' ', '')))

if len(data[0]) == len(data[1]):
    for i in range(len(data[0])):
        if data[0][i] != data[1][i]:
            print('NO')
            quit()

    print('YES')
else:
    print('NO')
    
    
    




