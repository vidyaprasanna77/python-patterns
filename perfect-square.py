def square (a):
    if a%(a**0.5) == 0 :
        return 1
    else:
        return 0 

print(square(4))