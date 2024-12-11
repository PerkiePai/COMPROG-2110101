import numpy as np
def mult_table(nrows, ncols):
    l1=[[i for i in range(1,ncols+1)] for j in range(1,nrows+1)]
    l2=[[j for i in range(ncols)] for j in range(1,nrows+1)]
    return np.array(l1)*np.array(l2)
# print(mult_table(12,12))
exec(input().strip())