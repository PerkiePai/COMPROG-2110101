def bisection_log10(a):
    L = 0
    U = 0
    temp = a
    while temp >= 10:
        temp //= 10
        U += 1
    U += 1 

    while (U - L) > 1e-10:
        mid = (L + U) / 2
        if 10**mid > a:
            U = mid
        else:
            L = mid
            
    return round(mid,6)


a = float(input())
result = bisection_log10(a)
print(result)
