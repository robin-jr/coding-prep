class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.addSuffix(self.root, string[i:])
    
    def addSuffix(self,root, suffix):
        if not suffix: 
            root["*"] = True
            return
        e = suffix[0]
        if not root.get(e): root[e] = {}
            
        return self.addSuffix(root[e],suffix[1:])

    def contains(self, string, root=None):
        if not root: root = self.root
        if not string:  
            return True if root.get("*", False) else False
        e = root.get(string[0])
        if not e: return False
        return self.contains(string[1:], root[string[0]])
    

