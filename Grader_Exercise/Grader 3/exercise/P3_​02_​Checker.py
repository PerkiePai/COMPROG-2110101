check=input().strip()

def checkColor(row,col):
    allrow='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    isWhite=True
    if allrow.find(row)%2==1:
        isWhite=False
    if int(col)%2==0:
        isWhite=not isWhite
    if isWhite: return 'White'
    return 'Black'

def checkShort(s1,row,col):
    allrow='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allcol=' 0123456789'
    isValidRow=True
    isValidCol=True
    if row not in allrow:
        isValidRow=False
    for i in range(1,len(s1)):
        if s1[i] not in allcol:
            isValidCol=False
    if isValidCol:
        if col=='' or int(col)>52 or int(col)<=0:
            isValidCol=False
    if not isValidRow and not isValidCol:
        print('Invalid row and column')
        return False
    elif not isValidRow:
        print('Invalid row')
        return False
    elif not isValidCol:
        print('Invalid column')
        return False
    return True

def checkLong(s1):
    l1=s1.split(",")
    l1=[e.strip().split('=') for e in l1]

    d1={}
    isValidRow=True
    isValidCol=True
    allrow='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allcol=' 0123456789'
    for e in l1:
        d1[e[0].strip()]=e[1].strip()
    #print(d1)
    
    if d1['row'] not in allrow or len(d1['row'])!=1:
        isValidRow=False
    for i in range(1,len(d1['col'])):
        if d1['col'][i] not in allcol or len(d1['col'])>2:
            isValidCol=False
    if isValidCol:
        if d1['col']=='' or int(d1['col'])>52 or int(d1['col'])<=0:
            isValidCol=False
    
    if not isValidRow and not isValidCol:
        print('Invalid row and column')
        return False
    elif not isValidRow:
        print('Invalid row')
        return False
    elif not isValidCol:
        print('Invalid column')
        return False
    return True

    

def long2(s1):
    l1=s1.split(",")
    l1=[e.strip().split('=') for e in l1]
    d1={}
    for e in l1:
        d1[e[0].strip()]=e[1].strip()
    s1=d1['row']+d1['col']
    return s1

if len(check)<=3:
    row=check[0]
    col=check[1:]
    if checkShort(check,row,col):
        print(checkColor(row,col))
else:
    if checkLong(check):
        row=long2(check)[0]
        col=long2(check)[1:]
        print(checkColor(row,col))
        


