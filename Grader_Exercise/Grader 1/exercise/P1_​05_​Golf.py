import math

def input_score():
    
    total_parr=0
    total_stroke=0
    total_fixed_stroke=0
    
    for i in range(9):
        score=input().split()
        total_parr+=int(score[0])
        total_stroke+=int(score[1])
        if score[2]=='1':
            fixed_stroke=min(int(score[0])+2,int(score[1]))
            total_fixed_stroke+=fixed_stroke
            
    return total_parr,total_stroke,total_fixed_stroke


total_parr,total_stroke,total_fixed_stroke = input_score()
handicap = math.floor(0.8*(1.5*total_fixed_stroke-total_parr))

print(total_stroke)
print(handicap)
print(total_stroke-handicap)
            