n=int(input())
a=[int(x) for x in input().split(" ")]
e=[]
o=[]
for i in a:
    if i%2==0:e.append(i)
    else:o.append(i)
print(e,o)
"""
o/p:
8
1 2 4 5 6 7 8 9
[2, 4, 6, 8] [1, 5, 7, 9]
"""
