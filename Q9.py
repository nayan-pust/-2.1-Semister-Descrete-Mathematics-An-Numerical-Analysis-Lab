


#Problem No. 09
#Name of the Problem: The values of y and x are given as below:
    
    #x: 5 6 9 11
    #y: 12 13 14 16

#Write a program to find the value of y when x=10 using Lagrange’s interpolation formula.



def lagrange(x, y, value, n):
    yp = 0
    for i in range(n):
        pro = 1
        for j in range(n):
            if i != j:
                pro *= (value - x[j]) / (x[i] - x[j])
        yp += pro * y[i]
    return yp


n = 4
x = [5, 6, 9, 11]
y = [12, 13, 14, 16]
value = 10
print(lagrange(x, y, value, n))




#Output: 
#Value of f(10) is: 14.666666666666666
