from typing import List


class Solution:
    def hasCommonLetters(self, a: str, b: str) -> bool:
        for e in a:
            if e in b:
                return True
        return False
    
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key= lambda x: len(x))
        n = len(words)
        max_product = 0
        for i in range(n-1):
            for j in range(i,n):
                if not self.hasCommonLetters(words[i],words[j]):
                    lengths_product = len(words[i])* len(words[j])
                    max_product =  lengths_product if lengths_product >max_product else max_product
        return max_product


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]
s = Solution()
x = s.maxProduct(words)
print(x)