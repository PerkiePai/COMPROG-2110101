import math

a,b,c=[e for e in input().strip().split(',')]

numerator = int(a+b+c) - int(a+b)
denominator = 10**(len(b)+len(c)) - 10**len(b)
gcd = math.gcd(numerator,denominator)
print(numerator//gcd,"/",denominator//gcd)
