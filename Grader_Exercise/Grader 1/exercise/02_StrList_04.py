m=int(input())
n=int(input())

i=max(len(str(m)),n)
ans='0'*n+str(m)
ans=ans[-i:]
print(ans)