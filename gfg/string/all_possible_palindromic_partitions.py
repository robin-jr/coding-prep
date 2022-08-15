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
            
def palindromic_partitions1(arr: list[str]):
    res = set()
    res.add(tuple(arr))
    if len(arr)<=1: return res
    
    for i in range(1, len(arr)):
        if arr[i-1]==arr[i][::-1]: 
            t = arr[:i-1] + [arr[i-1]+ arr[i]]+arr[i+1:]
            res.update(palindromic_partitions1(t))
        elif i+1<len(arr) and arr[i-1]==arr[i+1][::-1]:
            t = arr[:i-1]+[arr[i-1]+arr[i]+arr[i+1]]+arr[i+2:]
            res.update(palindromic_partitions1(t))
    return res

s = "nitin"
all = []
palindromic_partitions(s, all, [], 0)
print(all)

x = palindromic_partitions1(list(s))
print(list(x))

