n=int(input())
n1=0
n2=1
r=[]
print(n1,n2,end=" ")
for i in range(n):
    n3=n1+n2
    n1=n2
    n2=n3
    r.append(n3)
print(*r)
        
o/p:
10
0 1 1 2 3 5 8 13 21 34 55 89
