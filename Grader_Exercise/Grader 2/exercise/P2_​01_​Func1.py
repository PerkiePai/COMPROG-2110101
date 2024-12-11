def is_odd(n):
# คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่
    if n%2==1:
        return True
    else:
        return False


def has_odds(x):
# คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลบางตัวเป็นจ านวนคี่
    for i in x:
        if i%2==1:
            return True
    return False

def all_odds(x):
# คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลทุกตัวเป็นจ านวนคี่
    for i in x:
        if i%2==0:
            return False
    return True

def no_odds(x):
# คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข ้อมูลที่เป็นจ านวนคี่เลย
    for i in x:
        if i%2==1:
            return False
    return True

def get_odds(x):
# คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์ x (ล าดับก่อนหลังให ้เป็นไปตามล าดับเดียวกับใน x)
# เชน่ x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]
    output = []
    for i in x:
        if i%2==1:
            output.append(i)
    return output

def zip_odds(a, b):
# คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
# เชน่ a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได ้คือ
# [1,19,5,11,7,17,9,3]
    a = get_odds(a)
    b = get_odds(b)
    output = []
    n=0
    
    if len(a)==0:
        output = b
        return output
    elif len(b)==0:
        output = a
        return output
    else:
        for i in range(min(len(a),len(b))):
            output.append(a[i])
            output.append(b[i])
            n=i
        if len(a)>len(b):
            for e in range(n+1,len(a)):
                output.append(a[e])
        else:
            for e in range(n+1,len(b)):
                output.append(b[e])     
        return output
        
    
exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
