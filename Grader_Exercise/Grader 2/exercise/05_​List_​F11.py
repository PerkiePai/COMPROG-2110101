def missing_digits(t):

    num = ['0','1','2','3','4','5','6','7','8','9']

    atleast = 0
    found = 0

    output = []
    for i in range(10):
        for j in range(len(t)):
            if t[j] == num[i]:
                found = 1
                atleast = 1
        if found == 0:
            output.append(int(num[i]))
        found = 0
        
    if atleast == 0:
        return '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
    else:
        return output
        
exec(input()) # DON'T remove this line