def convex_polygon_area(p):
    p.append(p[0])
    sum1,sum2 = 0,0
    for i in range(0,len(p)-1):
        sum1 += p[i][0]*p[i+1][1]
    for i in range(1,len(p)):
        sum2 += p[i][0]*p[i-1][1]
    area = 0.5*((sum1)-(sum2))
    return abs(area)


def is_heterogram(s):
    s = s.lower()
    unwanted_chars = [',', ' ', '(', ')', '{', '}', '[', ']', "'"]
    for i in unwanted_chars:
        s = s.replace(i,'')
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True
    
def replace_ignorecase(s, a, b):
    lower_s = s.lower()
    lower_a = a.lower()
    result = ''
    i = 0
        
    while True:
        if i > len(s)-len(a):
            break
        else:
            if lower_s[i:i+len(a)] == lower_a:
                result += b
                i += len(b)-1
            else:
                result += s[i]
        i+=1
    result += s[i:]
    
    return result
    
def top3(votes):
    return [v for k,v in sorted([(-v,k) for k,v in votes.items()])[:3]]


for k in range(2):
    exec(input().strip())
