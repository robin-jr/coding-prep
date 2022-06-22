def checkPalindrome(t:int,string: str):
    x = string[t]
    i = t-1 
    j = t+1
    while i >=0 and j < len(string) and string[i]==string[j]:
        x = string[i]+x + string[j]
        i-=1
        j+=1
    return x

def checkPalindromeEven(t: int, string: str):  
    x = ""
    i = t-1 
    j = t
    while i >=0 and j < len(string) and string[i]==string[j]:
        x = string[i]+x + string[j]
        i-=1
        j+=1
    return x

def longestPalindromicSubstring(string: str):
    longest = string[0]
    for i in range(1,len(string)):
        t1 = checkPalindrome(i, string)
        t2 = checkPalindromeEven(i, string)
        print(t1,t2)

        if len(t1) > len(longest): longest = t1
        if len(t2) > len(longest): longest = t2
        
    return longest

string = "abaxyzzyxf"
x = longestPalindromicSubstring(string)
print(x)