def reverse(d):
    b = dict(zip(d.values(),d.keys()))
    return b

def keys(d, v):
    l1 = [e for e in d if d[e] == v]
    return l1

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ