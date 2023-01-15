


#Problem No. 08
#Name of the Problem: Write a program to find the value of f(15) from the following 
#table using Newton’s divided difference formula for unequal intervals.
#x: 4 5 7 10 11 13
#f(x): 48 100 294 900 1210 2028



def proTerm(i, value, x):
    pro = 1
    for j in range(i):
        pro *= (value - x[j])
    return pro


def diffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = (y[j + 1][i - 1] - y[j][i - 1]) / (x[i + j]-x[j])
    return y


def applyFormula(x, y, value, n):
    sum = y[0][0]
    for i in range(1, n):
        sum += (proTerm(i, value, x)) * y[0][i]
    return sum


def printDiffTable(x, y, n):
    for i in range(n):
        print(x[i], end='\t')
        for j in range(n - i):
            print("{:8.2f}".format(y[i][j]), end='\t')
        print('')


n = 6
y = [[0 for i in range(n)] for j in range(n)]
x = [4, 5, 7, 10, 11, 13]
y[0][0] = 48
y[1][0] = 100
y[2][0] = 294
y[3][0] = 900
y[4][0] = 1210
y[5][0] = 2028
y = diffTable(x, y, n)
printDiffTable(x, y, n)
value = 15
print("Value at ", value, 'is = ', applyFormula(x, y, value, n))



#output

#4          48.00           52.00           15.00            1.00            0.00            0.00
#5         100.00           97.00           21.00            1.00            0.00
#7         294.00          202.00           27.00            1.00
#10        900.00          310.00           33.00
#11       1210.00          409.00
#13       2028.00
#Value at  15 is =  3150.0
