import sys
from numpy import *
r1,c1=[int(a) for a in input().split()]
r2,c2=[int(a) for a in input().split()]
if c1!=r2:
    print("multiplication not pssible")
    sys.exit()
str1=input("first matix")
x=reshape(matrix(str1),(r1,c1))
str2=input("second matix")
y=reshape(matrix(str2),(r2,c2))
print("product")
z=x*y
print(z)
"""
o/p:
2 3
3 2
first matix1 2 3 4 5 6
second matix1 0 0 2 1 -1
product
[[ 4  1]
 [10  4]]
"""
