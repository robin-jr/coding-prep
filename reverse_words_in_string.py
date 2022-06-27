def reverseWordsInString(string):
    r = []
    s = -1
    for j in range(len(string)):
        if string[j]==" ": 
            r.insert(0,string[s+1:j])
            r.insert(0," ")
            s = j
        
    r.insert(0,string[s+1:])
    return "".join(r)

w = "AlgoExpert  is the best!"
x = reverseWordsInString(w)
print(x)