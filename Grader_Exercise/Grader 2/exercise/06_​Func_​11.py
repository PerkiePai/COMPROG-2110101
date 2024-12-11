b1, b2 = [int(e,2) for e in input().split()]

b3 = b1+b2
b3 = bin(b3)

print(b3[2:])