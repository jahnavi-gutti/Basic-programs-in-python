n=int(input())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
print(*a)

"""
o/p:
15
1 3 5 15
"""
