word = input().strip()

string = list(input())

punc = ['"' , '(' , ')' , ',' , '.' , "'"]
output = ''

for i in range(len(string)):
    if string[i] in punc:
        output += ' '
    else:
        output += string[i]

count=0
words = output.strip().split()
for w in words:
    if w == word:
        count+=1
print(count)
