#include <bits/stdc++.h>

using namespace std;

int binarySearch(vector<int> array, int target)
{
    int n = array.size();
    int m;
    int l = 0;
    int h = n - 1;
    while (l<=h)
    {
        m=(l+h)/2;
        if (array[m] == target)
        {
            return m;
        }
        else if (array[m] < target)
        {
            l = m+1;
        }
        else
        {
            h = m-1;
        }
    }
    return -1;
}

int main()
{
    vector<int> a = {0, 1, 21, 33, 45, 45, 61, 71, 72, 73};
    int x = binarySearch(a, 33);
    cout << x;
}