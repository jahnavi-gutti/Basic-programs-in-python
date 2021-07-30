a=[int(x) for x in input().split(" ")]
e=0
o=0
for i in a:
    if i%2==0:
        e+=1
    else:
        o+=1
print(e,o)
"""
o/p:
1 2 3 3 5 6 7 8
3 5
"""
