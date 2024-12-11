string = input().strip().upper()
char = input().strip()

correct = {'A':'T','T':'A','G':'C','C':'G'}

def check_valid(string):
    for i in string:
        if i not in correct:
            print('Invalid DNA')
            return False
    return True

if check_valid(string):
    if char == 'R':
        out=''
        for i in string:
            out+=correct[i]
        print(out[::-1])
        
    elif char == 'F':
        dict = {}
        string = sorted([char for char in string])
        check = string[0]
        count = 0
        for i in correct.keys():
            for j in string:
                if i == j:
                    count+=1
            dict[i]=count
            count=0
        print(f"A={dict['A']}, T={dict['T']}, G={dict['G']}, C={dict['C']}")
        
    elif char == 'D':
        check = input().strip().upper()
        count=0
        for i in range(len(string)-len(check)+1):
            if check==string[i:i+len(check)]:
                count+=1
        print(count)
            
            
            
            
            
            
            
            
            
            
