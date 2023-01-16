

  
  
  #Problem No. 02
#Name of the Problem: Suppose that 𝐴 = {1, 2, 3} and 𝐵 = {1, 2}. Let R be the relation 
#from A to B containing (a, b) if 𝑎 ∈ 𝐴, 𝑏 ∈ 𝐵, and 𝑎 > 𝑏. Write a program to find the relation 
#R and also represent this relation in matrix form if 𝑎1 = 1, 𝑎2 = 2, and 𝑎3 = 3, and 𝑏1 = 1 and 
#𝑏2 = 2. 




from itertools import product
import numpy as np

a = [1, 2, 3]
b = [1, 2]

res = [(i, j) for i, j in product(a, b) if i > j]
res2 = [1 if i > j else 0 for i in a for j in b]
data = np.array(res2).reshape(3, 2)

print(res)
print(data)





#Output:
#Enter First file name with extension: data4.txt
#Enter Second file name with extension: data5.txt
#R = [(2, 1), (3, 1), (3, 2)]
#Matrix, R = 

Procedure: This program start with “import numpy as np”. NumPy is a Python library used for 
working with arrays. In Python we have lists that serve the purpose of arrays, but they are slow to 
process. NumPy aims to provide an array object that is up to 50x faster than traditional Python 
lists. The means of “import numpy as np” is Now the NumPy package can be referred to 
as np instead of numpy.
Firstly, I created two files data4.txt file and data5.txt file in the same folder and here putted values 
of the sets for getting input. Now, for getting input from data4.txt file, I used input function for 
getting input and assigned the first file with a variable named file_name1. After that I used open 
method and also used file mode “r” for reading the file and putted the first file with a variable 
named file1. Similarly, I putted the second file name with a difference variable named file_name2 
and also assigned the second file with a difference variable named file2.
After that, I used map function. It has received two parameters, such as function and iterable object, 
it returns a list and I putted the list with a variable named list1. I used the same things again, but 
this time I putted the student.txt file with a different variable named file2 and also putted the list 
with a different variable named list2.
Afterwards, I used list comprehension for calculating some specific mathematical tasks. First task 
is putted with a variable named output and second task is putted with a variable named output2.
Then I used an attribute from numpy named np.array and putted the result with a variable named 
arr. After that, I used reshaping array that means changing the shape of an array. I used 
arr.reshape(3,2) and putted the result with a variable named newarr. Lastly, I printed the result.
# [0 0]
 #[1 0]
 #[1 1]
