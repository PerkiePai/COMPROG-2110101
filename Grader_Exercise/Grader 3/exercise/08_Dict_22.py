stocks = {}
sales = {}


N = int(input())
for i in range(N):
    line = input().strip().split()
    stocks[line[0]]=int(line[1])
M = int(input())
for i in range(M):
    line = input().strip().split()
    if line[0] in sales:
        sales[line[0]]+=int(line[1])
    else:
        sales[line[0]]=int(line[1])

output = {}
for sale in sales:
    if sale in stocks:
        output[sale]=sales[sale]*stocks[sale]
total_sales=float()
if output=={}:
    print('No ice cream sales')
    quit()

for k in output:
    total_sales+=output[k]
print(f'Total ice cream sales: {total_sales}')

output=[[k,v] for k,v in output.items()]
top=sorted(sorted(output),key=lambda a:-a[1])
print(f'Top sales: {top[0][0]}',end='')
for i in range(1,len(output)):
    if top[i][1] != top[i-1][1]:
        break
    else:
        print(f', {top[i][0]}',end ='')


            
    