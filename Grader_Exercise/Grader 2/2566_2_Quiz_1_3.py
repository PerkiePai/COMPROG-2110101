pattern = input()
N = int(input())

for _ in range(N):
    found = False
    count = 0
    string = input()
    for i in range(len(string)-len(pattern)+1):
        if pattern == string[i:i+len(pattern)]:
            if pattern == string[i+len(pattern):i+2*len(pattern)]:
                found = True
                for j in range(i,len(string)-len(pattern)+1,len(pattern)):
                    if pattern == string[j:j+len(pattern)]:
                        count+=1
                    else:
                        break
                break
    if found:
        print(count)
    else:
        print(0)


# inp = input()
# n = int(input())
# for i in range(n):
#     ans = 0
#     x = input()
#     x = x.replace(inp,"*")
#     idx = x.find("*")
#     if idx == -1:
#         print(0)
#         continue
#     while idx < len(x) and x[idx] == '*':
#         idx+=1
#         ans+=1
#     if ans ==1:
#         print(0)
#     else :
#         print(ans)
่
        
    