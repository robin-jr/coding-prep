#include <iostream>
#include <vector>
using namespace std;
class Solution
{
private:
    void swap(vector<int> &a, int i, int j)
    {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
    int partition(vector<int> &a, int l, int p)
    {
        int b = l - 1;
        for (int i = l; i <= p; i++)
        {
            if (a[i] <= a[p])
                swap(a, i, ++b);
        }
        return b;
    }

public:
    void quickSort(vector<int> &a, int l, int h)
    {
        if (h <= l)
        {
            return;
        }

        int p = partition(a, l, h);
        quickSort(a, l, p - 1);
        quickSort(a, p + 1, h);
    }
    void print(vector<int> &a)
    {
        for (auto &&e : a)
        {
            cout << e << " ";
        }
        cout << "\n";
    }
};

int main()
{
    Solution s = Solution();
    vector<int> a = {4, 3, 2, 1};
    s.quickSort(a, 0, a.size() - 1);
    s.print(a);
}