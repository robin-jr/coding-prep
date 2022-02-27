#include <bits/stdc++.h>

using namespace std;

vector<int> findThreeLargestNumbers(vector<int> array)
{
    int l1 = INT_MIN;
    int l2 = INT_MIN;
    int l3 = INT_MIN;

    for (auto &&el : array)
    {
        if (el > l3)
        {
            l1 = l2;
            l2 = l3;
            l3 = el;
        }
        else if (el > l2)
        {
            l1 = l2;
            l2 = el;
        }
        else if (el > l1)
        {
            l1 = el;
        }
    }
    return {l1, l2, l3};
}

int main()
{
    vector<int> a = {141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7};
    vector<int> b = findThreeLargestNumbers(a);
    for (auto &&i : b)
    {
        cout << i << " ";
    }
}
