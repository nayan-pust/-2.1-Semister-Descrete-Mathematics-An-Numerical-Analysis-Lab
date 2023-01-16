


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

Procedure: The program started with a class named ‘Data’. Under this class I created a
parameterized constructor. This constructor has received two parameters, namely, x and y. I used 
a comment above the constructor for easily understanding this codes. Constructors are generally 
used for instantiating an object. The task of constructors is to initialize (assign values) to the data 
members of the class when an object of class is created. I assigned the receivable x and y into this 
class variable x and y respectively, this means self.x = x and self.y = y.
After that, I created a user defined function named ‘interpolate’. It has received three parameters, 
namely, f, xi and n. f: list means f is a list as well as xi: int and n: int means xi and n are integer. 
Also I used a type converter symbol (->), that’s mean all of the parameterized variables type is 
change to be float. Under this function I created a variable named result and assign the value is 
result = 0.0. 
x: 5 6 9 11
y: 12 13 14 16
Under interpolate function I also used a ‘for’ loop. Under this for loop I declared a variable named 
‘term’ and compute individual terms of Lagrange’s Interpolation formula and assigned the value 
into ‘term’ variable. This ‘for’ loop is execute n times which is the interpolate function variable n.
After that, I used another for loop under first for loop that’s mean I used nested for loop. This for 
loop is also execute n times. Under this for loop I used ‘if’ condition, if the condition is true then 
Lagrange’s Interpolation formula will be evaluated. This process execute continues until the 'for' 
loop is false. Then put the term variable value into the result variable. This process is continues n 
times that’s mean four times because the value of n is four. And finally returned the result variable.
Afterwards, I created a list named ‘f’ and into the list I called the Data class and also initialized 
the value. I called the Data class four times.
Finally, I called the interpolate function with given three arguments and same time also printed the 
interpolate function.
