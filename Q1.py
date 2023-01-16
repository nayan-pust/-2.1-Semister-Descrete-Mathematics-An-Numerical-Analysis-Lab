

#Problem No. 01
#Name of the Problem: Let A be the set 𝐴 = {1, 2, 3, 4}. Write a program to find the ordered 
#pairs are in the relation I) 𝑅1 = {(𝑎, 𝑏) | 𝑎 𝑑𝑖𝑣𝑖𝑑𝑒𝑠 𝑏} II) 𝑅2 = {(𝑎, 𝑏) | 𝑎 ≤ 𝑏}.



from itertools import product

s = list(map(int, input().split()))

res = [(i, j) for i, j in product(s, repeat=2) if i % j == 0]
res2 = [(i, j) for i, j in product(s, repeat=2) if i <= j]

print("The pair order a/b : " + str(res))
print("The pair order a<=>b : " + str(res2))





  #input =1 2 3 4
  
  
  #output=
#The pair order a/b : [(1, 1), (2, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 2), (4, 4)]
#The pair order a<=>b : [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

Procedure: Firstly, from the itertools module I used product method. The itertools.product() is 
used to find the cartesian product from the given iterator.
After that, I created a data3.txt file in the same folder and then created a variable file_name in the 
present python file and given a message through the input () function for taking input. I putted the
input file into a new variable named ‘file’. I used open function to open the file and also used file 
mode “r” for reading this file. Then I used map function, usually map function receive two 
parameters, such as function and iterable object (such as, list) and map function basically returns 
iterable object itself. I put the list with a variable named S. After that, I printed the values of S. 
Afterwards I used two comprehension list for two mathematical calculation and put the result with 
two variable. Then I printed the result. Lastly, I closed the file.
