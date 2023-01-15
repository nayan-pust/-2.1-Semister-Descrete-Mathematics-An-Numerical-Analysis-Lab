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
