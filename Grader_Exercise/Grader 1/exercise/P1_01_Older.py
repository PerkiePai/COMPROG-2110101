nick1, m1, d1, y1 = [i for e in input().split(',') for i in e.split()]
nick2, m2, d2, y2 = [i for e in input().split(',') for i in e.split()]

d1, y1 = int(d1), int(y1)
d2, y2 = int(d2), int(y2)

def m_to_num(m):
    for i in range(12):
        months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if m == months_list[i]:
            m = i+1
            return m
        
def check(name1,name2):
    if y1<y2:
        return name1
    if y1>y2:
        return name2
    
    if m_to_num(m1)<m_to_num(m2):
        return name1
    if m_to_num(m1)>m_to_num(m2):
        return name2
    
    if d1<d2:
        return name1
    if d1>d2:
        return name2
    
    return f'{name1} {name2}'

print(check(nick1,nick2))
