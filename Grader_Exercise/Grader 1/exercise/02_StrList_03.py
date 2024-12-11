dmy = input()
dmy = dmy.split('/')
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(months_list[int(dmy[1])-1], dmy[0]+',', dmy[2])

