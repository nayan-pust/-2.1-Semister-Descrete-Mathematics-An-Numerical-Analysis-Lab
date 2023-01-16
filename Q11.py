


#11. Write a program to find a root of the function 
#x𝟐 − 𝒙 − 𝟐 = 𝟎 in the range 1<x<3 using false 
#position method.

INT_MAX = 100000


def fun(x):
    return (x * x - x - 2)


def falsi(a, b):
    if fun(a) * fun(b) > 0:
        print("Invalid")
        return
    c = a
    for i in range(INT_MAX):
        c = (a * fun(b) - b * fun(a)) / (fun(b) - fun(a))
        if fun(c) == 0.0:
            break
        if fun(a) * fun(c) < 0:
            b = c
        else:
            a = c
    print("The Value of Root is : {:.4f}".format(c))


a = 1
b = 3
falsi(a, b)




    #Output:
    #The Value of Root is : 2.0000

    Procedure: At first, I initialized MAX_ITER = 1000000. Then I created a user defined 
function named func, it has received one parameter x and returned x * x * x – 2 * x – 5.
After that, I created another user define function named regulaFalsi, it has received two parameters 
a and b. Under this function I used an if condition for checking whether func(a) * func(b) >=0. If 
this condition is true then print function would be executed and return -1. Then I assigned variable 
a into variable c.
Afterwards, I used for loop for evaluating some tasks. Under for loop first task was found the 
point that touches x axis that’s mean evaluated the c. Then I used if condition under this for loop 
for checking the found point is whether root or not. If this condition is match then break keyword 
would be worked. But if this condition is not match then elif (else if) condition would be worked. 
Under this elif condition I checked whether func(c) * func(a) < 0. If this elif condition is matched 
then variable c would be assigned into variable b. But if this elif condition is not matched then 
finally else condition would be worked.
Then, I printed the variable c. When I printed variable c I used %.4f that’s mean float formatting 
number with fixed width 4.
At last, I initiazed values of variable a and b. And finally I called the regulaFalsi functio
