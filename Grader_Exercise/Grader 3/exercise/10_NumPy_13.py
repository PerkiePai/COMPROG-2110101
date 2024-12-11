import numpy as np
import math
def p(X):
    logit = -3.98 + (0.1*X[:,0]) + (0.5*X[:,1])
    p = 1/(1 + math.e**(-logit))
    return p
exec(input().strip())