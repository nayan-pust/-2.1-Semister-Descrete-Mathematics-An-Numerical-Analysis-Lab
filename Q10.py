



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
