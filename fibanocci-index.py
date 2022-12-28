# 0 1 1 2 3 5 8 13  21....
# 0 1 2 3 4 5 6 7  8 ... index 

i = 8 
a = 0 
b = 1 

for x in range(i-1):
    c = a + b
    a = b 
    b = c 
print(c)