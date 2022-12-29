import math 
R = int(input("enter the radius"))

def sphere(R):

    return (math.ceil((4 * math.pi * R**3)/3))


print(sphere(R))