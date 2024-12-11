def grade(g):
    grade = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    return grade.get(g,0)

def is_pass(stu):
    is_pass = stu[2] == 'A' and grade(stu[3]) >= 2 and grade(stu[4]) >= 2
    return is_pass

def choose(stu1, stu2):
    if not is_pass(stu1) and not is_pass(stu2):
        return []
    if is_pass(stu1) and not is_pass(stu2):
        return [stu1[0]]
    if not is_pass(stu1) and is_pass(stu2):
        return [stu2[0]]
    
    if stu1[1] > stu2[1]:
        return [stu1[0]]
    if stu1[1] < stu2[1]:
        return [stu2[0]]
    
    if grade(stu1[3]) > grade(stu2[3]):
        return [stu1[0]]
    if grade(stu1[3]) < grade(stu2[3]):
        return [stu2[0]]
    
    if grade(stu1[4]) > grade(stu2[4]):
        return [stu1[0]]
    if grade(stu1[4]) < grade(stu2[4]):
        return [stu2[0]]
    
    return [stu1[0], stu2[0]]

exec(input()) # DON'T remove this line