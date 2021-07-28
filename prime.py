n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print("prime")
else:
    print("not prime")
"""
o/p:
6
not prime
3
Prime
"""
