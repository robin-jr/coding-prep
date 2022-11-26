d = {}
def ambiguousMeasurements(measuringCups, low, high):
    global d
    d= {}
    return helper(measuringCups , low, high)
    

def helper(measuringCups, low, high):
    if (low,high) in d: 
        return d[(low,high)]
    if low <0 and high < 0 :
        d[(low,high)] = False
        return False
    for cup in measuringCups:
        if low<=cup[0] and high>=cup[1]:
            d[(low,high)] = True
            return True
        if helper(measuringCups, low-cup[0], high-cup[1]):
            d[(low,high)] = True
            return True

    d[(low,high)] = False
    return False