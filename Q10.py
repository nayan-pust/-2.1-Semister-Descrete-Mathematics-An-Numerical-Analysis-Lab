



#10 Write a program to find a real root of the equation 
#x𝟐 − 𝟒𝐱 − 𝟏𝟎 = 𝟎 that lies between -2 and 
#-1.5 using bisection method


INT_MAX = 100000


def fun(x):
    return (x * x  - 4 * x - 10)




def bisection(a, b):
    if fun(a) * fun(b) > 0:
        print("You have not assumed right a and b\n")
        return
    c = a
    for i in range(INT_MAX):
        c = (a + b) / 2
        if fun(c) == 0.0:
            break
        if fun(a) * fun(c) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ", "{:.4f}".format(c))


a = -2
b = -1.5
bisection(a, b)



#output:

#The value of root is :  -1.7417

Procedure: This program started with a user define function named func. It has received only 
one parameter x and returned x*x*x-2x-5.
After that, I used another user defined function named bisection function. It has received two 
parameters a and b. Under this function I used an ‘if’ condition, if this condition is true then print 
function would be execute and also return -1. Otherwise, variable a assigned into variable c.
Then, I used a while loop with a condition, (b – a) >= 0.0001. If this condition is true then some 
tasks would be executed. Under this while loop firstly, I found the middle point c. Afterwards, I 
used an if condition for checking whether middle point is root or not. If this condition is true then 
break keyword would be executed and while loop would be dismissed. Then I again used an if
condition below the first the if condition. If first if condition is false just then this if condition is 
executed but if first if condition is true then this if condition would not be executed. Finally, I 
printed the variable c. When I printed variable c I used %.4f that’s mean float formatting number 
with fixed width 4.
At last, I initiazed values of variable a and b. And finally I called the bisection function
