t = int(input("enter the number of test cases"))
for i in range(t):
    n = int(input("enter the integer:"))
    result = 0 
    while n != 0 :
        digit = n%10 
        result = result * 10 +digit 
        new = n//10 
        n = new
    print(result)
