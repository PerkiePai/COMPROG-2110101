key = input()

ans1 = key[3] + key[10] + key[17] + key[24] + key[31]
ans2 = key[7] + key[12] + key[17] + key[22] + key[27]
ans3 = str(int(ans1) + int(ans2) + 10000)
ans4 = ans3[-4:-1]
ans5 = str(int(ans4[0]) + int(ans4[1]) + int(ans4[2]))
ans6 = int(ans5[-1]) + 1

chars = ['A','B','C','D','E','F','G','H','I','J']

ans7 = chars[ans6-1]

ans = ans4+ans7

print(ans)