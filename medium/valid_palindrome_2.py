class Solution:
    def validPalindrome(self, s: str, deletion_count=0) -> bool:
        n=len(s)
        if n<2: return deletion_count<=1
        if deletion_count>1: return False
        while s[0]==s[-1] and n>2:
            s=s[1:n-1]
            n-=2
        if s[0]==s[-1]: return True
        return self.validPalindrome(s[1:n], deletion_count+1) or self.validPalindrome(s[0:n-1], deletion_count+1)
    
s = "cupuupucua"
print(Solution().validPalindrome(s))
 
