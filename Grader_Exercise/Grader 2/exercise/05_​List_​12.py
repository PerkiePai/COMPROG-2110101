N = int(input())

name = [input() for e in range(N)]

realname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

for i in range(N):
    if name[i] in realname:
        print(nickname[realname.index(name[i])])
    elif name[i] in nickname:
        print(realname[nickname.index(name[i])])
    else:
        print('Not found')