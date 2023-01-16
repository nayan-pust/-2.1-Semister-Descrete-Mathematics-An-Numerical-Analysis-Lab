
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

Procedure: At first, I initialized INF = 1000000000. Then, I declared a function named 
floyd_warshall, it has received two parameters, vertex and adjacency_matrix. After that, I used 
three ‘for’ loop (nesting style) for calculating some specific tasks. Every for loop range is 0 to 
vertex. Last for loop that’s mean most inner for loop task is find minimum adjacency_matrix 
between the “adjacency_matrix[i][j]” and “adjacency_matrix[i][k] + adjacency_matrix[k][j]”.
Afterwards, I used print function. Then I again used for loop. Under the ‘for’ loop I used print 
function. Inside the print function I used string formatting command {:d}. It is used to string 
number (integer) formatting. After that, I used again print function but this time it is not under the 
‘for’ loop.
Then I again used another ‘for’ loop and under the ‘for’ loop I took print function and another ‘for’
loop in nesting style. Under the inner for I used print function and print the adjacency matrix. 
Afterwards I again used simple print function.
After that, I initialized the adjacency matrix. Then called the floyd_warshall function
