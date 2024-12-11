data = [int(e) for e in input().split()]

data.sort()
count=1
output=[]
output.append(data[0])

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count+=1
        if len(output)<10:
            output.append(data[i+1])
        
print(count)
print(output)