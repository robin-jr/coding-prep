def isValidPart(string):
    t = int(string)
    if len(string) != len(str(t)) : return False
    if t>=0 and t<= 255: return True
    return False

def helper(string,parts=[]):
    res = []
    if not string and len(parts)==4: 
        res.append(".".join(parts))
        return res
    
    if string and len(parts)==4: return res
    
    if not string : return res
    
    for i in range(1,4):
        part = string[:i]
        if isValidPart(part):
            t = parts+ [part]
            res += helper(string[i:],t)
            
    return res

def validIPAddresses(string):
    return list(set(helper(string)))

string  = "192160800"
x = validIPAddresses(string)
for e in x:
    print (e)
print(len(x))