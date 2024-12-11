n = int(input())
list01 = [int(input()) for _ in range(n)]

list02 = [int(e) for e in input().split()]

list03 = []
while True:
    data = int(input())
    if data == -1:
        break
    list03.append(data)

merge_list = list01+list02+list03

output=[]
for i in range(len(merge_list)):
    if i%2==0:
        output.append(merge_list[i])
    else:
        output.insert(0,merge_list[i])
print(output)