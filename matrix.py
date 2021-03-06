"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math
import copy
#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end =' ')
        print("\n")

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(i==j):            
                matrix[i][j]=1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    copym2=copy.deepcopy(m2)
    for i in range(len(m1)):
        for j in range(len(m2[i])):
            m2[i][j]=point(i,j,m1,copym2)

def point(x,y,m1,m2):
    total=0
    hold=0
    for j in range(len(m1)):
        hold=m1[x][j]*m2[j][y]
        total+=hold
    return total
            


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
