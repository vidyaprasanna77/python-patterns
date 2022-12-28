# 0 1 1 2 3 5 8 13....

N = int(input())
a = 0 
print(a)
b = 1 
print(b)
c = a+b 

while c<N:
    print(c)
    a = b 
    b = c
    c = a + b 
