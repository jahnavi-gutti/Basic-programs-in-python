a=[int(x) for x in input().split(" ")]
e=0
o=0
for i in a:
    if i%2==0:
        e+=i
    else:
        o+=i
print(e,o)
"""
o/p:
1 2 3 4 5 6 2
14 9
"""
