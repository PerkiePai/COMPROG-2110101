str_input = input()

output=''

output+=str_input[0]
count=1
for i in range(1,len(str_input)):
    if str_input[i]!=str_input[i-1]:
        output+=' '+str(count)+' '+str_input[i]
        count=1
    else:
        count+=1
output+=' '+ str(count)
print(output)
            

    