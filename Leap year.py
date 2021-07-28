n=int(input())
if n%400==0 or (n%4==0 and n%100!=0):
    print("leap year")
else:
    print("not leap year")
"""
o/p:
2020
leap year
2018
not leap year
"""
