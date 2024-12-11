def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def gcd1(a,b,c):
    a=gcd(gcd(gcd(a,b),gcd(a,c)),gcd(b,c))
    return a

def is_coprime(a, b, c):
    if gcd1(a,b,c)==1:
        return True
    return False

def primitive_Pythagorean_triples(max_len):
    l1=[]
    for i in range(3,max_len-1):
        for j in range(i+1,max_len):
            for k in range(j+1,max_len+1):
                if i**2+j**2==k**2:
                    if is_coprime(i,j,k):
                        l1.append([i,j,k])
                    
    return sorted(l1,key=lambda a:a[2])

exec(input().strip())
        

