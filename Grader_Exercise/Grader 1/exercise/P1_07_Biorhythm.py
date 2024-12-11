import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]

def day_start(d, m, y):
    d_in_m1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    d_in_m2 = [31,29,31,30,31,30,31,31,30,31,30,31]

    y -= 543
    sum=d_in_m1[m-1]-d

    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        for i in range(m,12):
            sum += d_in_m2[i]
        if m<=2 and d<=28:
            sum += 1
    else:
        for i in range(m,12):
            sum += d_in_m1[i]
    
    return sum+1

def day_last(d, m, y):
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
    
    return sum-1

def day_between(by,y):
    y = max(0,y-by-1)
    d = 365*y
    return d

t = day_start(bd, bm, by) + day_between(by,y) + day_last(d, m, y)

def phys(t):
    phys = math.sin((2*math.pi*t)/(23))
    return phys
    
def emot(t):
    emot = math.sin((2*math.pi*t)/(28))
    return emot
    
def inte(t):
    inte = math.sin((2*math.pi*t)/(33))
    return inte
    
print(str(t) , "{:.2f}".format(phys(t)) , "{:.2f}".format(emot(t)) , "{:.2f}".format(inte(t)) )
    
    
    
