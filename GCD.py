def gcd(A,B):
    while B%A != 0:
        r = B%A 
        B = A 
        A = r 
    return A

print(gcd(12,15))