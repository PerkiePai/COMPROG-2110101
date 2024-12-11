n,y = input().strip().split()
with open('data/data.txt','r') as f:
    l1=[]
    while True:
        line = f.readline()
        if line=='':
            break
        line = line.split()
        l1.append([line[1],line[0]])
        
    l2=[]
    for i in range(len(l1)):
        if y[-2:] == l1[i][1][:2]:
            l2.append([l1[i][0],l1[i][1]])
    if l2==[]:
        print('No data')
        quit()
    l2 = sorted(l2)
    l3 = [float(k) for k,v in l2]
    print(f'{l2[0][0]} {l2[-1][0]} {sum(l3)/len(l3)}')

        