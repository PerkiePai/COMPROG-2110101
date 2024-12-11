def text2keys( text ):
    d1={'abc': '2', 'def': '3', 'ghi': '4', 'jkl': '5', 'mno': '6', 'pqrs': '7', 'tuv': '8', 'wxyz': '9',' ': '0'}
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    text=list(text.lower())
    out=''
    for char in text:
        if char in alphabet:
            for key in d1.keys():
                if char in key:
                    index=key.index(char)
                    for i in range(index+1):
                        out+=d1[key]
                    out+=' '
    return out.strip()
    
def keys2text( keys ):
    d2={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
    keys=keys.split()
    out=''
    for char in keys:
        index=len(char)-1
        out+=d2[char[0]][index]
    return out

# ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
exec(input().strip())



