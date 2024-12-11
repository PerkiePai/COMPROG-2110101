def read_matrix():
    A = [[float(e) for e in input().split()] for i in range(int(input()))]
    return A

def mult_c(c, A):
    A = [[c*i for i in e] for e in A]
    return A


def mult(A,B):
    C=[]
    for i in range(len(A)):
        c=[]
        for j in range(len(B[0])):
            sum=0
            for k in range(len(B)):
                sum+=A[i][k]*B[k][j]
            c.append(sum)
        C.append(c)
    return C
    

exec(input().strip())

