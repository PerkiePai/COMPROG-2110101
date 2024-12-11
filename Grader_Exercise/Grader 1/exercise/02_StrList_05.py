sales = input()
sales = sales.split()
sum=0

for i in range(len(sales)):
    sum=sum+int(sales[i])
    
print(sum)