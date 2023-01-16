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

Procedure: This program started with a user defined function named u_cal. It has received two 
parameters, u and n. Under this function, firstly I created a variable named temp and assign the 
value of u. Then I used ‘for’ loop, under this loop I done some specific task and putted the result 
in temp variable. Lastly, I returned the temp variable.
After that, I again used another user defined function named “fact” for calculating factorial of 
given number n. 
Afterwards, I declared n variable and assigned the value 6. Then I declared an array named x. After 
that, I used comprehension list and putted the result in variable y.
Subsequently, I assigned y[0][0]=12; y[1][0]=15; y[2][0]=20; y[3][0]=27; y[4][0]=39; y[5][0]=52.
For calculating the forward difference table I used two ‘for’ loop in nesting style. Then I again 
used two for loop in nesting style for displaying the forward difference table.
After that, I created a variable named ‘value’ and assigned the interpolated value 1946. Then I 
created another variable named sum and initializing sum = y[0][0]. Again, I created variable named 
‘u’ and calculated some specific task and putted the result in variable ‘u’.
Afterwards, I used for loop and calculated some specific tasks and putted the final result in variable 
some. Here, I called two user defined u_cal and fact function. 
Lastly, I printed the sum variable, here I used round function. The round () function returns a 
floating point number that is a rounded version of the specified number, with the specified number 
of decimals
