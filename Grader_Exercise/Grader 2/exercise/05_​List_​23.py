import math

n = int(input())

coordinates = []

for i in range(n):
    data = [float(e) for e in input().strip().split()]
    ranges = math.sqrt(data[0]**2 + data[1]**2)
    data.insert(0,ranges)
    data.insert(1,i)
    
    coordinates.append(data)

coordinates.sort()
    
index1, index2, index3, index4 = coordinates[2]
    
print('#'+str(index2+1)+': '+'('+str(index3)+', '+str(index4)+')')
    
    