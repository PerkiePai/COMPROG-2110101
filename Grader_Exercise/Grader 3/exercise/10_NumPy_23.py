import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    n=np.ndarray(4,)
    for i in range(1,4):
        n[i]=np.sum(data[:,1:]*weight[i-1],axis=1)
    m=np.mean(n)
    return [n for e in n if n<m]
