#include <iostream>
using namespace std;
class Solution
{
public:
    bool isPalindrome(int x)
    {
        int a = x;
        if (x < 0)
        {
            return false;
        }
        long long unsigned t = 0;
        while (x)
        {
            t = (x % 10) + (t * 10);
            x /= 10;
        }
        return t == a;
    }
};

int main()
{
    Solution s = Solution();
    bool x = s.isPalindrome(12121);
    cout << x;
}