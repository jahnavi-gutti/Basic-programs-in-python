n=int(input())
m=n
s=0
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
while(n!=0):
    d=n%10
    s+=f(d)
    n=n//10
if s==m:
    print("given no is special no")
else:
    print("given no is not special no")
"""o/p:
145
given no is special no
35
given no is not special no
"""    
   
