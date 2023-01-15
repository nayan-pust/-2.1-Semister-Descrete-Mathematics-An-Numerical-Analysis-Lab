
#Problem No. 04
#Name of the Problem: Write a program to find shortest path by Warshall’s algorithm.



INF = 1000000000


def warshell(vertex, adjmatrix):
    for k in range(vertex):
        for i in range(vertex):
            for j in range(vertex):
                adjmatrix[i][j] = min(adjmatrix[i][j], adjmatrix[i][k] + adjmatrix[k][j])
    print('o/d', end='')
    for i in range(vertex):
        print("\t{:d}".format(i + 1), end='')
    print()
    for i in range(vertex):
        print('{:d}'.format(i + 1), end='')
        for j in range(vertex):
            print("\t{:d}".format(adjmatrix[i][j]), end='')
        print()


adjacency_matrix = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
warshell(4, adjacency_matrix)


    
    
    #output
    
    
    #o/d     1       2       3       4
#1       0       5       8       9
#2       1000000000      0       3       4
#3       1000000000      1000000000      0       1
#4       1000000000      1000000000      1000000000      0
