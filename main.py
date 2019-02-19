from display import *
from draw import *
from matrix import *
from random import randint

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
print("Testing ident. m1 =")
ident(matrix)
print_matrix(matrix)
m=[[],[],[],[]]
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = ")
add_edge(m,1,2,3,4,5,6)
print_matrix(m)
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(matrix,m)
print_matrix(m)
m2=[[],[],[],[]]
print("Testing Matrix mult. m1 =")
add_edge(m2,1,2,3,4,5,6)
add_edge(m2,7,8,9,10,11,12)
print_matrix(m2)
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m2,m)
print_matrix(m)
add_edge(matrix,50,50,0,100,100,0)
for i in range(100):
    add_edge(matrix,randint(0,500),randint(0,500),0,randint(0,500),randint(0,500),0)
print_matrix(matrix)
draw_lines( matrix, screen, color )
display(screen)
