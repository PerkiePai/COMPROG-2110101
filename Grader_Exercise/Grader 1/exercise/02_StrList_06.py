a = input()
b = input()

a = a.strip('[]').split(',')
b = b.strip('[]').split(',')

a = list(map(float, a))
b = list(map(float, b))

c = []

for i in range(3):
    c.append(a[i] + b[i])

print(a,'+',b,'=',c)
