n=int(input())
a=[]
for i in range(1,n):
    if n%i==0:
        a.append(i)
if sum(a)==n:
    print("perfect no")
else:
    print("not perfect")
"""
o/p:
15
not perfect
6
perfect no
"""
