n=int(input())
e=0
o=0
while(n!=0):
    d=n%10
    if d%2==0:
        e+=1
    else:
        o+=1
    n=n//10
print(e,o)
"""
o/p:
12346
3 2
"""
