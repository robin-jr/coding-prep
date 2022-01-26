
#include <iostream>
#include <string>
#include <vector>

using namespace std;
class Solution
{
public:
    bool isValid(string s)
    {
        vector<char> a;
        for (auto &&c : s)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                a.push_back(c);
            }
            else if (a.empty())
            {
                return false;
            }
            else
            {
                char lastChar = a[a.size() - 1];
                if ((lastChar == '(' && c != ')') || (lastChar == '[' && c != ']') || (lastChar == '{' && c != '}'))
                {
                    return false;
                }
                a.pop_back();
            }
        }
        return a.empty();
    }
};
int main()
{
    Solution s = Solution();
    int x = s.isValid("()[{}]");
    cout << x;
}