

  
  
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
# [0 0]
 #[1 0]
 #[1 1]
