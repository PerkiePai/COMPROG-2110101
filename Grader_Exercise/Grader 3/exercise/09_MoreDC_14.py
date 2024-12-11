with open(input(),'r') as f1:
    with open(input(),'r') as f2:
        with open(input(),'r') as f3:
            f1=[e for e in f1.readlines()]
            f1=[e.strip() for e in f1]
            f1=[e.split(',') for e in f1]
            d1={}
            for e in f1:
                d1[e[0]]=e[1]
            f2=[e for e in f2.readlines()]
            f2=[e.strip() for e in f2]
            f2=[e.split(',') for e in f2]
            d2={}
            for e in f2:
                d2[e[0]]=e[1]
            f3=[e for e in f3.readlines()]
            f3=[e.strip() for e in f3]
            f3=[e.split(',') for e in f3]
            for e in f3:
                if e[0] in d1 and e[1] in d2:
                    print(f'{d1[e[0]]},{d2[e[1]]}')
                else:
                    print('record error')
            
            