N = int(input().strip())

name_nick={}
nick_name={}
for i in range(N):
    data = input().strip().split()
    name_nick.update({data[0]:data[1]})
    nick_name.update({data[1]:data[0]})
    
M = int(input().strip())

for i in range(M):
    ask = input().strip()
    if ask in name_nick:
        print(name_nick[ask])
    elif ask in nick_name:
        print(nick_name[ask])
    else:
        print("Not found")