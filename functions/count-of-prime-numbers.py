def solve(A):
    def isprime(n):
        if n < 2:
            return 0 
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return 0 
        return 1 

    count = 0 
    for i in A :
        count = count + isprime(i)
    return count 


A = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,166,25]
print(solve(A))