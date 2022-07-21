def groupAnagrams(words):
    sorted_words = []
    for i in range(len(words)):
        sorted_words.append(sorted(words[i]))
    
    hashMap = {}
    for i in range(len(sorted_words)):
        word = ''.join(sorted_words[i])
        hashMap[word] =hashMap.get(word, []) + [words[i]]
    
    return list(hashMap.values())

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
x = groupAnagrams(words) 
print(x)
        
