#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    bool validMountainArray(vector<int> &arr)
    {
        if (arr.size() < 3)
        {
            return false;
        }
        bool rising = true;
        int i = 1;
        while (i < arr.size())
        {
            int diff = arr[i] - arr[i - 1];
            if (diff < 0)
            {
                if (i == 1)
                {
                    return false;
                }
                rising = false;
            }
            if (diff == 0)
            {
                return false;
            }
            if (diff < 0 && rising)
            {
                return false;
            }
            if (diff > 0 && !rising)
            {
                return false;
            }
            i += 1;
        }
        return !rising;
    }
};

int main()
{
    vector<int> a = {1, 2, 3};
    Solution s = Solution();
    bool x = s.validMountainArray(a);
    cout << x;
}
