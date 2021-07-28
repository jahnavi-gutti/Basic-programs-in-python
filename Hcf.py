def hcf(x, y):
    smaller=min(x,y)
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i  
    return hcf  
num1 = int(input())  
num2 = int(input())  
print(hcf(num1, num2))  
