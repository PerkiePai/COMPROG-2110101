data = input().strip()

unwanted_chars = [',', '(', ')', '{', '}', '[', ']', "'",'"','.','>',';','-']

for c in unwanted_chars:
    data = data.replace(c,' ')

data = data.lower()
data = data.split()

output = ''
for c in data:
    output += c[0].upper()+c[1:]
    
print(output[0].lower()+output[1:])



