num1 = int(input())
num2 = int(input())
Max=max(num1,num2)
while(True):
    if(Max % num1 == 0 and Max % num2 == 0):   
        print(Max)
        break;
    Max= Max+ 1
    """
o/p:
3
8
24
"""
