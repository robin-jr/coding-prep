def minimumCharactersForWords(words):
    d = {}
    
    for word in words:
        t = {}
        for char in word:
            t[char] = t.get(char, 0) + 1
        
        for k,v in t.items():
            d[k] = max(d.get(k, 0) , v)
    r = []
    for e,f in d.items():
        r.extend([e]*f)
    return r

words = ["this", "that", "did", "deed", "them!", "a"]
x = minimumCharactersForWords(words)
print(x)