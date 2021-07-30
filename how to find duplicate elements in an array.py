 how to find duplicate elements in an array
def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated
list1 = [int(x) for x in input().split(" ")]
print (Repeat(list1))
"""
o/p:
1 2 3 3 4 5 4 6
[3, 4]
"""

