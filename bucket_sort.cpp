#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
private:
public:
    void bucketSort(vector<int> &a, int bucketSize)
    {
        vector<int> bucket[bucketSize] = {};
        for (auto &&val : a)
        {
            int i = val / bucketSize;
            bucket[i].push_back(val);
        }
        int k = 0;
        for (int i = 0; i < bucketSize; i++)
        {
            sort(bucket[i].begin(), bucket[i].end());
            for (int j = 0; j < bucket[i].size(); j++)
            {
                a[k++] = bucket[i][j];
            }
        }
    }
    void print(vector<int> &a)
    {
        for (auto &&i : a)
        {
            cout << i << " ";
        }
        cout << "\n";
    }
};
int main()
{
    Solution s = Solution();
    vector<int> a = {3, 2, 5, 1, 7, 4, 4, 0, 0, -2};
    s.bucketSort(a, 3);
    s.print(a);
}