with open('data1.txt') as f:
    f1=f.read()
    print(f1)
    
with open('data1.txt') as f:
    f1=f.readline()
    print(f1)
    
with open('data1.txt') as f:
    f1=f.readlines()
    print(''.join(f1))