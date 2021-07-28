n1,n2=input().split()
n1,n2=int(n1),int(n2)
for i in range(1,min(n1,n2)+1):
    if n1%i==n2%i==0:
        print(i)
"""o/p:
6 12
1
2
3
6
"""
