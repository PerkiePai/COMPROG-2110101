def match(w,p,cin,cout):
    check=True
    if len(w)!=len(p):
        check=False
    else:
        for i in range(len(w)):
            if p[i] != '?':
                if p[i] != w[i]:
                    check=False
            else:
                if p[i] in cout:
                    check=False
                    
        for i in range(len(w)):
            if p[i]=='?':
                if w[i] not in cin:
                    check=False
    return check

exec(input())
    
    