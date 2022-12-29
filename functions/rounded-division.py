
def solve(a):
    temp = a /200
    ans = a //200 
    # for positive values
    if temp > 0:    
        x = temp - ans 
        if x >=0.5:
            return(ans+1)
        else:
            return ans
    # for negative values 
    elif temp < 0:
        x = temp - ans 
        if x>0.5:
            return(ans+1)
        else:
            return ans 

    else:
        return("0")
    

print(solve(2578))