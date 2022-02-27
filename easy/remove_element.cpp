#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution
{
private:
public:
    int removeElement(vector<int> &nums, int val)
    {
        int k = 0, n = nums.size(), i = 0;
        for (; i < n; i++)
        {
            if (nums[i] != val)
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
    vector<int> a = {0, 1, 2, 2, 3, 0, 4, 2};
    // vector<int> a={3,2,2,3};
    int x = s.removeElement(a, 2);
    cout << x;
}