s11 =input()
s22 =input()
s1=sorted(list(s11.strip().lower()))
s2=sorted(list(s22.strip().lower()))

alphabet = "abcdefghijklmnopqrstuvwxyz"
def count(s1):
    d1={}
    for char in s1:
        if char in alphabet:
            if char in d1:
                d1[char]+=1
            else:
                d1[char]=1
    return d1

d1 = count(s1)
d2 = count(s2)

def output(d1,d2):
    if d1==d2:
        return print(' - None')
    else:
        k1 = [k for k in d1.keys()]
        k2 = [k for k in d2.keys()]
        check=[]
        for k in k1:
            if k in d2:
                if d1[k]>d2[k]:
                    check.append('0')
            else:
                check.append('0')               
        if check == []:
            return print(' - None')
        else:
            for k in d1.keys():
                if k in d2:
                    if d1[k]-d2[k]==1:
                        print(f" - remove {d1[k]-d2[k]} {k}")
                    elif d1[k]-d2[k]>1:
                        print(f" - remove {d1[k]-d2[k]} {k}'s")
                else:
                    if d1[k]==1:
                        print(f" - remove {d1[k]} {k}")
                    elif d1[k]>1:
                        print(f" - remove {d1[k]} {k}'s")
         
    
print(s11)
output(d1,d2)
print(s22)
output(d2,d1)

