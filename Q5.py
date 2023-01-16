#Problem No. 05
#Name of the Problem: Suppose that the relations R1 and R2 on a set A are represented 
#by the matrices 
#𝑴𝑹𝟏 = [
#𝟏 𝟎 𝟏
#𝟏 𝟎 𝟎
#𝟎 𝟏 𝟏
#] and 𝑴𝑹𝟏 = [
#𝟏 𝟎 𝟏
#𝟎 𝟏 𝟏
#𝟏 𝟎 𝟏
#]. Write a program to find the 𝑴𝑹𝟏∪𝑹𝟐 and 𝑴𝑹𝟏∩𝑹𝟐.


def intersection(mat1, mat2):
    intersect = [[(mat1[i][j] and mat2[i][j]) for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return intersect


def union(mat1, mat2):
    uni = [[(mat1[i][j] or mat2[i][j]) for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return uni


matrix1 = [[1, 0, 1],
           [1, 0, 0],
           [0, 1, 1]]
matrix2 = [[1, 0, 1],
           [0, 1, 1],
           [1, 0, 1]]
print("Matrix A: ", matrix1)
print("Matrix B: ", matrix2)
mi = intersection(matrix1, matrix2)
mu = union(matrix1, matrix2)
print("Matrix intersection: ", mi)
print("Matrix Union: ", mu)
v = ['p', 'q', 'r']
r1 = [(v[i], v[j]) for i in range(len(mi)) for j in range(len(mi[0])) if mi[i][j] == 1]
r2 = [(v[i], v[j]) for i in range(len(mu)) for j in range(len(mu[0])) if mu[i][j] == 1]
print(r1)
print(r2)




#Matrix A:  [[1, 0, 1], [1, 0, 0], [0, 1, 1]]
#Matrix B:  [[1, 0, 1], [0, 1, 1], [1, 0, 1]]
#Matrix intersection:  [[1, 0, 1], [0, 0, 0], [0, 0, 1]]
#Matrix Union:  [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
#[('p', 'p'), ('p', 'r'), ('r', 'r')]
#[('p', 'p'), ('p', 'r'), ('q', 'p'), ('q', 'q'), ('q', 'r'), ('r', 'p'), ('r', 'q'), ('r', 'r')]

Procedure: At first, I declared a function named matrix_intersection. It has received two 
parameters mat1 and mat2. Then I declared two variables rows and cols as well as evaluate the 
length of the rows and cols. After that, I printed the length of rows and cols. Afterwards, I declared 
an empty array named mat_inter. Then I used ‘for’ loop and calculating some specific tasks (matrix 
intersection) and lastly returned the mat_inter array. 
After that, I declared another function named matrix_union. It has also received two parameters. 
Then I declared another empty array named mat_union. Afterwards, I used ‘for’ loop for 
calculating some specific tasks (matrix union) and lastly returned mat_union function. Then I 
initialized the matrix1 and matrix2. After that, I printed the matrix1 and matrix2.
Afterwards, I called the matrix_intersection function and putted the result with a variable named 
mi and then printed the mi variable.After that, I called the matrix_union function and putted the result with a variable named mu and 
lastly printed the mu variable.
Then I initialized a string and putted the value with a variable named v. After I declared an empty 
array named r1. Afterwards, I declared a for loop and inside the for loop I declared another for 
loop and also used ‘if” condition, if the condition is true I appended the some specific value with 
r1. After that, I printed the r1.
Then, I declared another empty array named r2. I used above process again and lastly I printed the 
r2 variable
