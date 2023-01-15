


#Problem No. 07
#Name of the Problem: Write a program to find f(7.5) form the following table using 
#Newton-Gregory backward interpolation formula. 
#x: 1 2 3 4 5 6 7 8
#f(x): 1 8 27 64 125 216 343 512



def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u + i)
    return temp


def fact(n):
    f = 1
    for j in range(1, n + 1):
        f *= j
    return f


n = 8
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 1
y[1][0] = 8
y[2][0] = 27
y[3][0] = 64
y[4][0] = 125
y[5][0] = 216
y[6][0] = 343
y[7][0] = 512

for i in range(1,n):
    for j in range(n-1, i-1, -1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

for i in range(n):
    print(x[i], end='\t')
    for j in range(i + 1):
        print("{:4d}".format(y[i][j]), end='\t')
    print('')

value = 7.5
u = ((value - x[n - 1]) / (x[1] - x[0]))
sum = y[n - 1][0]
for i in range(1, n):
    sum += (u_cal(u, i) * y[n - 1][i]) / fact(i)
print("f({:.2f})".format(value), "=", sum)



  
  #output

#1          1
#2          8       7
#3         27      19      12
#4         64      37      18       6
#5        125      61      24       6       0
#6        216      91      30       6       0       0
#7        343     127      36       6       0       0       0
#8        512     169      42       6       0       0       0       0
#f(7.50) = 421.875
