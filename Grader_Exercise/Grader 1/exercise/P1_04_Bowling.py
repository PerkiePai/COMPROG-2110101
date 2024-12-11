result=input()
code=int(input())

total = 0
frame = 1
index = 0

def translate(i):
    if i >= len(result):
        return 0
    elif result[i] == 'X':
        return 10
    elif result[i] == '/':
        return 10 - int(result[i-1])
    else:
        return int(result[i])

def calculate(frame, index):
    if frame == 10:
        score = translate(index) + translate(index + 1) + translate(index + 2)
        frame += 1
        index += 2 if result[index] != 'X' else 1
        return score, frame, index
    elif result[index] == 'X':
        score = 10 + translate(index + 1) + translate(index + 2)
        frame += 1
        index += 1
        return score, frame, index
    elif result[index] and result[index + 1] == '/':
        score = 10 + translate(index + 2)
        frame += 1
        index += 2
        return score, frame, index
    elif result[index].isdigit() and result[index + 1].isdigit():
        score = translate(index) + translate(index + 1)
        frame += 1
        index += 2
        return score, frame, index
    
for _ in range(1, 11):
    if code==frame:
        total=0
        score, frame, index = calculate(frame, index)
        print(score)
        quit()
    score, frame, index = calculate(frame, index)
    total += score
    
print(total)
    

