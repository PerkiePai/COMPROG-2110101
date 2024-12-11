pas = input().strip()


def eightLetter(pas):
    if len(pas)>=8: return True
    else: return False
    
def hasLower(pas):
    lower = "abcdefghijklmnopqrstuvwxyz"
    hasLower = False
    for i in pas:
        if i in lower:
            hasLower = True
            break
    return hasLower

def hasUpper(pas):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasUpper = False
    for i in pas:
        if i in upper:
            hasUpper = True
            break
    return hasUpper

def hasNum(pas):
    num = "0123456789"
    hasNum = False
    for i in pas:
        if i in num:
            hasNum = True
            break
    return hasNum
    
def hasSym(pas):
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '=', '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']
    hasSym = False
    for i in pas:
        if i in symbol:
            hasSym = True
            break
    return hasSym
    
def charRep(pas):
    pas1 = pas.lower()
    lower = "abcdefghijklmnopqrstuvwxyz"
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '=', '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']
    num = "0123456789"
    ischarRep = False
    if len(pas1)<4:
        return ischarRep 
    else:
        for i in range(len(pas1)-3):
            if pas1[i] in lower or pas1[i] in symbol or pas1[i] in num:
                if pas1[i] == pas1[i+1] == pas1[i+2] == pas1[i+3]:
                    ischarRep = True
                    break
        return ischarRep    
    
def numSeq(pas):
    isNumSeq = False
    num1 = "01234567890"
    num2 = "09876543210"
    pas1 = pas
    if len(pas1)<4:
        return isNumSeq
    else:
        for i in range(len(pas1)-3):
            if pas1[i] in num1:
                index = num1.index(pas1[i])
                if pas1[i:i+4] == num1[index:index+4]:
                    isNumSeq = True
                    break
                index = num2.index(pas1[i])
                if pas1[i:i+4] == num2[index:index+4]:
                    isNumSeq = True
                    break
        return isNumSeq

def letSeq(pas):
    isLetSeq = False
    pas1 = pas.lower()
    lower1 = "abcdefghijklmnopqrstuvwxyz"
    lower2 = "zyxwvutsrqponmlkjihgfedcba"
    if len(pas1)<4:
        return isLetSeq
    else:
        for i in range(len(pas1)-3):
            if pas1[i] in lower1:
                index = lower1.index(pas1[i])
                if pas1[i:i+4] == lower1[index:index+4]:
                    isLetSeq = True
                    break
                index = lower2.index(pas1[i])
                if pas1[i:i+4] == lower2[index:index+4]:
                    isLetSeq = True
                    break
        return isLetSeq
    
def keyPat(pas):
    ROW1 = "!@#$%^&*()_+"
    ROW2 = "QWERTYUIOP"
    ROW3 = "ASDFGHJKL"
    ROW4 = "ZXCVBNM"
    pas1 = pas.upper()
    isKeyPat = False
    if len(pas1)<4:
        return isKeyPat
    else:
        for i in range(len(pas1)-3):
            if pas1[i] in ROW1:
                if pas1[i:i+4] in ROW1:
                    isKeyPat = True
                    break
                if pas1[i:i+4] in ROW1[::-1]:
                    isKeyPat = True
                    break
            elif pas1[i] in ROW2:
                if pas1[i:i+4] in ROW2:
                    isKeyPat = True
                    break
                if pas1[i:i+4] in ROW2[::-1]:
                    isKeyPat = True
                    break
            elif pas1[i] in ROW3:
                if pas1[i:i+4] in ROW3:
                    isKeyPat = True
                    break
                if pas1[i:i+4] in ROW3[::-1]:
                    isKeyPat = True
                    break
            elif pas1[i] in ROW4:
                if pas1[i:i+4] in ROW4:
                    isKeyPat = True
                    break
                if pas1[i:i+4] in ROW4[::-1]:
                    isKeyPat = True
                    break
        return isKeyPat

if eightLetter(pas) and hasLower(pas) and hasUpper(pas) and hasNum(pas) and hasSym(pas) and not charRep(pas) and not numSeq(pas) and not letSeq(pas) and not keyPat(pas):
    print('OK')
else:
    if not eightLetter(pas): print("Less than 8 characters")
    if not hasLower(pas): print('No lowercase letters')
    if not hasUpper(pas): print('No uppercase letters')
    if not hasNum(pas): print('No numbers')
    if not hasSym(pas): print('No symbols')
    if charRep(pas): print('Character repetition')
    if numSeq(pas): print('Number sequence')
    if letSeq(pas): print('Letter sequence')
    if keyPat(pas): print('Keyboard pattern')

                
    
    
    