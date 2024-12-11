data = ''
uids = []
grades = []
uids2 = []

grade_list = ['A','B+','B','C+','C','D+','D','F']

while True:
    data = [e for e in input().split()]
    if data==['q']:
        break
    uids.append(data[0])
    grades.append(data[1])

data = input().split()
for i in range(len(data)):
    uids2.append(data[i])
    
def up_grades(id):
    if grades[uids.index(id)] == 'A':
        return 'A'
    else:
        if id in uids2:
            uid_index = uids.index(id)
            grades_index = grade_list.index(grades[uid_index])
            grades[uid_index] = grade_list[grades_index-1]
            return grades[uid_index]
        else:
            return grades[uids.index(id)]

for i in range(len(uids)):
    print(uids[i],up_grades(uids[i]))
            
            
    
    
    
    