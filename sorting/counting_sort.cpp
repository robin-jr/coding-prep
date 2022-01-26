#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class Solution
{
private:
public:
    void countingSort(vector<int> &a)
    {
        int max = *max_element(a.begin(), a.end());
        int count_arr[max + 1] = {};
        for (auto &&e : a)
        {
            count_arr[e] += 1;
        }
        int k = 0;
        for (int i = 0; i <= max; i++)
        {
            for (int j = 0; j < count_arr[i]; j++)
            {
                a[k++] = i;
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
    vector<int> a = {3, 2, 5, 1, 7, 4, 4};
    s.countingSort(a);
    s.print(a);
}