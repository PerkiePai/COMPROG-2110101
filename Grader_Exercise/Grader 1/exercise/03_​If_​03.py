a = list(map(float, input().split()))

sum = sum(a)
min = max = a[0]

for i in range(1,4):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
        
result = (sum - min - max) / 2

print(round(result, 2))
