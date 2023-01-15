#Problem No. 06
#Name of the Problem: The following table gives the population of a town during the last 
#six censuses. Write a program to find the population in the year of 1946 using Newton-Gregory forward interpolation formula. 
#Year: 1911 1921 1931 1941 1951 1961
#Population: 12 15 20 27 39 52


def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u - i)
    return temp


def fact(n):
    fac = 1
    for i in range(2, n + 1):
        fac *= i
    return fac


n = 6
x = [1911, 1921, 1931, 1941, 1951, 1961]
y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 12
y[1][0] = 15
y[2][0] = 20
y[3][0] = 27
y[4][0] = 39
y[5][0] = 52

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

for i in range(n):
    print(x[i], end='\t')
    for j in range(n-i):
        print(y[i][j], end='\t')
    print("")

value = 1946
u = (value - x[0]) / (x[1] - x[0])
sum = y[0][0]
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i] / fact(i))
print(sum)
   
   
   
   
  #output
  
  
  #1911    12      3       2       0       3       -10
#1921    15      5       2       3       -7
#1931    20      7       5       -4
#1941    27      12      1
#1951    39      13
#1961    52

#  value at !946 :32.34375

