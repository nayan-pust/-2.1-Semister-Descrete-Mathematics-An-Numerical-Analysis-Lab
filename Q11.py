


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
