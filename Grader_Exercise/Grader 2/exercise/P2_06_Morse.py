def T2M(t,d,line):
    out=''
    for char in line:
        out+=d[char]+' '
    return out.strip()

def M2T(t,d,line):
    out=''
    for char in line.split():
        out+=d[char]
    return out.strip()

def mToDict(m):
    m=m.replace('[',' ')
    m=m.replace(']',' ')
    m=m.strip().split()
    d1={}
    d2={}
    for i in range(0,len(m),2):
        d1[m[i]]=m[i+1]
        d2[m[i+1]]=m[i]
    return d1,d2
    

with open(input(),'r') as f:
    l1 = ['T2M','M2T']
    t=f.readline().strip('\n')
    if not t in l1:
        print('Invalid code')
    else: 
        m=f.readline().strip('\n')
        d1,d2=mToDict(m)
        while True:
            line=f.readline().strip('\n')
            if line=='':
                break
            elif t=='T2M':
                check=True
                for char in list(line):
                    if char not in d1:
                        print(f'Invalid : {line}')
                        check=False
                if check==True:
                    print(T2M(t,d1,line))
            elif t=='M2T':
                check=True
                line+=' '
                for char in line.split():
                    if char not in d2:
                        print(f'Invalid : {line}')
                        check=False
                if check==True:
                    print(M2T(t,d2,line))
                    
                

        

