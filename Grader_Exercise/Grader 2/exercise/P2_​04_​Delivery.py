def isValidYear(d,m,y):
    isYear = False
    if y>=2558:
        isYear=True
    return isYear

def isValidMonth(d,m,y):
    isMonth=False
    if m>0 and m<13:
        isMonth=True
    return isMonth
    
def isLeapYear(d,m,y):
    isLeap=False
    y-=543
    if y%400==0 or (y%4==0 and y%100!=0):
        isLeap=True
    return isLeap

common_year = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
delivery_type = {'E':1, 'Q':3, 'N':7, 'F':14}

def isValidDate(d,m,y):
    isDate=False
    if isLeapYear(d,m,y):
        index = m-1
        if d>0 and d<=leap_year[index]:
            isDate=True
    else:
        index = m-1
        if d>0 and d<=common_year[index]:
            isDate=True
    return isDate

def isValidType(t):
    isType=False
    if t in delivery_type:
        isType=True
    return isType

def addDate(t,d,m,y):
    total_day=0
    if isLeapYear(d,m,y):
        for i in range(m-1):
            total_day+=leap_year[i]
    else:
        for i in range(m-1):
            total_day+=common_year[i]
    total_day=total_day + d + delivery_type[t]
    if isLeapYear(d,m,y):
        if total_day>366:
            total_day-=366
            y+=1
    else:
        if total_day>365:
            total_day-=365
            y+=1
    m=0
    for i in range(12):
        if isLeapYear(d,m,y):
            if total_day<=leap_year[i]:
                d=total_day
                m=i+1
                break
            else:
                total_day-=leap_year[i]
        else:
            if total_day<=common_year[i]:
                d=total_day
                m=i+1
                break
            else:
                total_day-=common_year[i]
    return d,m,y

valid=[]
while True:
    line=input().strip()
    if line=='END':
        break
    else:
        name,t,d,m,y = line.split()
        d,m,y=int(d),int(m),int(y)
        if not isValidYear(d,m,y):
            print(f'Error: {line} --> Invalid year')
        elif not isValidMonth(d,m,y):
            print(f'Error: {line} --> Invalid month')
        elif not isValidDate(d,m,y):
            print(f'Error: {line} --> Invalid date')
        elif not isValidType(t):
            print(f'Error: {line} --> Invalid delivery type')
        else:
            d,m,y = addDate(t,d,m,y)
            valid.append([y,m,d,name,t])
        
valid = sorted(valid)
for line in valid:
    print(f'{line[3]}: delivered on {line[2]}/{line[1]}/{line[0]}')
        
        
            
    