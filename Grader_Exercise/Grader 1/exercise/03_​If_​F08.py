
def day_of_year(d, m, y):
    d_in_m1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    d_in_m2 = [31,29,31,30,31,30,31,31,30,31,30,31]

    y -= 543
    sum=d
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        for i in range(m-1):
            sum += d_in_m2[i]
    else:
        for i in range(m-1):
            sum += d_in_m1[i]
    
    return sum

exec(input()) # DON'T remove this line