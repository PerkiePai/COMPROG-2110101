x = [[e[0],int(e[1])] for e in [input().strip().split()]][0]
name,y = x[0],x[1]

with open(name, "r") as f:
    read_data = [[str(line.split()[0]), float(line.split()[1])] for line in f]
    l1 = [e for e in read_data if y%100 == int(e[0][:2])]
    if l1 == []:
        print('No data')
        quit()
    l2 = sorted(l1, key=lambda a:-a[1])
    print(f'{l2[-1][-1]} {l2[0][-1]} {sum(list(map(lambda x:x[1],l2)))/len(l2)}')
