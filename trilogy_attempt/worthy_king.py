def getDays(arr):
    x = 1
    day = 0
    troops = 0
    arr.sort()
    arr.reverse()
    daysToIncrement = 1
    while arr:
        daysToIncrement *= 2
        t =troops+ (x*daysToIncrement)
        if t > arr[-1]: 
            daysToIncrement = 1
            
        troops += x*daysToIncrement
        day += daysToIncrement
        
        for e in arr:
            if e <= troops: 
                arr.remove(e)
                troops = 0
                x += 1
                break
            
    return day
        

a = [4,3,1]
# a = [9,9]
a= [1000000000,10001]
# a = [1, 2, 4, 9]
x = getDays(a)
print(x)

# day x troops
# 1   1  1 
# 2   2  2 
# 3   3  3 
# 4   3  6 
# 5   3  9 
# 6   4  4