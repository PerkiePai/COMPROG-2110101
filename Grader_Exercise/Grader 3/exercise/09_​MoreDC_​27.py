def knows(R,x,y):
    isKnow = False
    if y in R[x]:
        isKnow = True
    return isKnow

def is_celeb(R,x):
    isCeleb=True
    if len(R[x])==0 or R[x]=={x}:
        for person in R:
            if x==person:
                continue
            if x not in R[person]:
                isCeleb=False
    else:
        return False
    return isCeleb

def find_celeb(R):
    check=False
    for person in R:
        if is_celeb(R,person):
            return person
    return None
    
def read_relations():
    R={}
    while True:
        d=input().split()
        if len(d)==1:
            break
        if d[0] in R:
            R[d[0]]=R[d[0]]|{d[1]}
        else:
            R[d[0]]={d[1]}
        if d[1] not in R:
            R[d[1]]=set()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input().strip())