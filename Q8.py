


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

Procedure: Firstly, I created a user define function called ‘u_cal’ for easily calculating and 
should be used ‘def’ for definition keyword before function name for created this. This function 
has received three parameters i, value and x. 
Primarily, I assigned to value of 1 with a variable named pro in the function named ‘u_cal’ and 
also created ‘for’ loop that ran value of i times. Inside this ‘for’ loop I created equation ‘pro * 
(value - x[j])’ and assigned with a variable named pro. Finally, I returned the result of pro. 
After that, I created a data.txt file in same folder and here putted values of the table x = [4, 5, 7, 
10, 11, 13] and f(x) = [48, 100, 294, 900, 1210, 2028] for getting input. Now, for reading the 
data.txt file primarily, I used input function for getting file name with extension from the user and 
putted the file name with a variable named file_name. Then I used open method and putted the file 
with a variable named file and also used read function for printed the values of file. After that I 
printed the values of table. 
Then I used a ‘split’ function for putted values of the data.txt file as a list with a variable named 
data. I created two empty lists with different variables named x and r. I used a zip function for 
append values of x with a variable named x and also append values of f(x) with a different variable 
named r in the empty list. Usually zip function has received two parameterssuch as iterables object, 
function and it returned a list. 
After that I initialized the values of population in the variable named y such as y[0][0] = 48, y[1][0] 
= 100, y[2][0] = 294, y[3][0] = 900, y[4][0] = 1210, y[5][0] = 2028 and I took value of x for 
interpolation from user using input function and assigned with a variable named value as a float 
number. 
After that, I calculated the divided difference table applying Newton’s divided difference formula 
for unequal interval y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j])) and printed the result of 
divided difference table. Afterwards, I assigned to value of y[0][0] with a variable named sum. 
Then I created a ‘for’ loop that ran length of table times. Inside the ‘for’ loop applying equation 
“sum + (u_cal(i,value,x) * y[0][i])” and assigned the result with a variable named sum. Here, the 
means of “u_cal(I, value, x)” is called function named ‘u_cal’ with three arguments such as i, value 
and x. 
Finally, I printed the result of sum for interpolation.
