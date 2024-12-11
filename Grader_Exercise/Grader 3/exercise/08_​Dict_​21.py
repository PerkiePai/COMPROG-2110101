st = input().strip().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in st:
    if char not in alphabet:
        st = st.replace(char,'')
st=sorted(list(st))
out=''
for char in st:
    out+=char
st=out
char=''
d=dict()
for i in range(len(st)):
    if char == st[i]:
        d[char]+=1
    else:
        char=st[i]
        d[char]=1

l1=list(zip(d.keys(),d.values()))
l1=sorted(l1)
l1=sorted(l1,key=lambda a:-a[1])

for a,b in l1:
    print(f'{a} -> {b}')




         