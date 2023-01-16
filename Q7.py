


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


Procedure: This program started with “from math import factorial”. Math is a Python library 
used for working with factorial calculation here. In Python we have long code that serve the 
purpose of factorial calculation, but they are timed and complexity to process. The means of “from 
math import factorial” is the math package can be referred to as factorial instead of math. Firstly, 
I created a data2.txt file in same folder and here putted values of the given table for getting input. 
Now, for reading the data.txt file primarily, I used input function for getting file name with 
extension from the user and putted the file name with a variable named file_name. 
Then I used open method and putted the file with a variable named file and also used read function 
for printed the values of file. After that I printed the values of table. Then I used a ‘split’ function 
for putted values of the data.txt file as a list with a variable named data. I created two empty lists 
with different variables named x and y. I used a zip function for append values of x with a variable 
named x and also append values of f(x) with a different variable named y in the empty list. Usually 
zip function has received two parameters such as iterables object and function and it returned a 
list. 
After that, I took value of x for interpolation from user using input function and assigned with a 
variable named inp as a float number. After that, I calculated the backward difference table 
applying Newton-Gregory backward interpolation formula. Primarily, I assigned to value of y with 
a variable named table as a list and I also created a ‘for’ loop that run ((length of y) – 1) times. 
Inside the ‘for’ loop I created an empty list with a variable named yn and also created a nested 
‘for’ loop that contained a zip function. In this ‘for’ loop calculated the equation (i - k) and append 
the result in the yn empty list. Finally, I append the result of yn in the variable named table and 
printed the result of backward difference table. Afterwards, I assigned to value of 1 with a variable 
named r_component and result of the formula “(inp - x[-1]) / (x[1] - x[0]) with a different variable 
named r and I also initialized ‘r_component = 0’. Then I created a ‘for’ loop that ran length of 
table times. Inside the ‘for’ loop applying equation “r_component * (r + i - 1)” and assigned the 
result with a variable named r_component and I also applying the equation “partial_result + 
(table[i][-1] * r_component) / factorial(i)” and assigned the result with a different variable named 
partial_result. 
Finally, I calculated the equation “table[0][-1] + partial_result” and assigned the result with a 
variable named final_result. At last, I printed the result of final_result for interpolation.
