def is_mobile_number(t):
    tel = ['06','08','09']
    
    if len(t) == 10 and t[0:2] in tel:
        return True
    else:
        return False

exec(input()) # DON'T remove this line