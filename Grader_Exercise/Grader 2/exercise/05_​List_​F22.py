
old_grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
new_grade = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]

def index_of(grades, ID):
    
    isHas = False
    index = 0
    
    for uid, grade in grades:
        if ID == uid:
            isHas = True
            break
        else:
            index+=1
        
    if isHas == True:
        return index
    else:
        return -1

def upgrade(grades, IDs):
    for uid in IDs:
        index = index_of(grades, uid)
        if index != -1:
            old = grades[index][1]
            index1 = old_grade.index(old)
            grades[index][1] = new_grade[index1]
    grades.sort()
            

exec(input())
exec(input())
exec(input())