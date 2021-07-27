n=int(input())
m=n
r=0
while(n!=0):
    d=n%10
    r=r*10+d
    n=n//10
if r==m:
    print("palindrome")
else:
    print("not palindrome")
