
def cut(list):
    lenght = len(list)
    cut_input=list[lenght//2:] 
    for i in range(0,lenght//2):
        cut_input.append(list[i])
    return cut_input
    
def shuffle(list):
    lenght = len(list)
    front_list = list[:lenght//2]
    back_list = list[lenght//2:]
    shuffle_list=[]
    a,b = 0,0
    for i in range(lenght):
        if i%2==0:
            shuffle_list.append(front_list[a])
            a+=1
        else:
            shuffle_list.append(back_list[b])
            b+=1
    return shuffle_list

input_list = input().strip().split()
process = input()
processed_list = []

for i in range(len(process)):
    if process[i] == 'C':
        input_list = cut(input_list)
    elif process[i] == 'S':
        input_list = shuffle(input_list)

print(input_list[0],end='')
for i in range(1,len(input_list)):
    print(' '+input_list[i],end='')