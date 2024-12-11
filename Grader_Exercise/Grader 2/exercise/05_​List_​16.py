n = int(input())

output_list = [n]

while n!=1:
    if n%2==0:
        n//=2
    else:
        n=3*n+1
    output_list.append(n)

output_list = output_list[-15:]

print(output_list[0],end='')
for i in range(1,len(output_list)):
    print('->'+str(output_list[i]),end='')