from display import *
from draw import *
from matrix import *
from random import randint

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix2 = new_matrix()

ident(matrix)
print_matrix(matrix)
ident(matrix2)
matrix_mult(matrix,matrix2)
m=[[125,26,0,0],[26,125,0,0],[0,26,125,0],[1,1,1,1]]
matrix_mult(m,matrix2)
print_matrix(matrix2)
add_edge(matrix2,50,50,0,100,100,0)
for i in range(100):
    add_edge(matrix2,randint(0,500),randint(0,500),0,randint(0,500),randint(0,500),0)
print_matrix(matrix2)
draw_lines( matrix2, screen, color )
display(screen)
