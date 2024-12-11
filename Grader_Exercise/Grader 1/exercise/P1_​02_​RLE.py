mode = input()
if mode!='str2RLE' and mode!='RLE2str':
    print('Error')
    exit;

str_input = input()

output=''
if mode=='str2RLE':
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
            
elif mode=='RLE2str':
    output=''
    str_input = str_input.split()
    for i in range(0,len(str_input),2):
        output+=str_input[i]*int(str_input[i+1])
    print(output)

else:
    print('Error')
    
    