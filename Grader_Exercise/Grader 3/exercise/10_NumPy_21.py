import numpy as np

def sum_2_rows( M ):
    return M[::2,:]+M[1::2,:]
def sum_left_right( M ):
    return M[::,:len(M[0])//2:]+M[::,len(M[0])//2::]
def sum_upper_lower( M ):
    return M[:len(M)//2,:]+M[len(M)//2:,:]
def sum_4_quadrants( M ):
    return M[:len(M)//2:,:len(M)//2:]+M[len(M)//2::,:len(M)//2:]+M[:len(M)//2:,len(M)//2::]+M[len(M)//2::,len(M)//2::]
def sum_4_cells( M ):
    return M[::2,::2]+M[1::2,::2]+M[::2,1::2]+M[1::2,1::2]  
def count_leap_years( years ):
    years-=543
    return len([e for e in years if (years % 400 == 0) or ((years % 100 != 0) and (years % 4 == 0))])

exec(input().strip())