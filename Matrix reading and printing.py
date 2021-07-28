R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")

for i in range(R):		
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	matrix.append(a)

for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()
"""
o/p:
Enter the number of rows:3
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
7
8
9
1 2 3 
4 5 6 
7 8 9
"""
