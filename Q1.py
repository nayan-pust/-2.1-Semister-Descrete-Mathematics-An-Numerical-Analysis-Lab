

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
