students=[]

while True:
    data = [e for e in input().strip().split()]
    if data[0] != 'q':
        students.append(data)
    else:
        break
    
upgrade_ID = input().split()

old_grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
new_grade = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]

for e in students:
    uid, grade = e[0] , e[1]
    if uid in upgrade_ID:
        e[1] = new_grade[old_grade.index(grade)]

students.sort()

for ID, grade in students:
    print(ID, grade)