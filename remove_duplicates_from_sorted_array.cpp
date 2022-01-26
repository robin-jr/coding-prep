
#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int n = nums.size();
        if (n < 1)
        {
            return n;
        }
        int current = nums[0];
        int k = 1;
        for (int i = 1; i < n; i++)
        {
            if (nums[i] != nums[i - 1])
            {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
int main()
{
    Solution s = Solution();
    vector<int> a = {1, 1, 2};
    int x = s.removeDuplicates(a);
    cout << x;
}