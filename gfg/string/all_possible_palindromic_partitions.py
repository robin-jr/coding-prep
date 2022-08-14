def isPalindrome(s: str):
    return s==s[::-1]

def palindromic_partitions(s: str, all, current, start: int):
    if start >= len(s): 
        all.append(current.copy())
        return
    for i in range(start, len(s)):
        t = s[start:i+1]
        if isPalindrome(t): 
            current.append(t)
            palindromic_partitions(s, all, current, i+1)
            current.pop()

all = []
palindromic_partitions("nitin", all, [], 0)
print(all)

