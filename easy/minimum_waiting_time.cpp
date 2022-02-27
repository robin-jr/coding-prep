#include <vector>
#include <bits/stdc++.h>

using namespace std;

int minimumWaitingTime(vector<int> queries)
{
    sort(queries.begin(), queries.end());
    int minTime = 0;
    int n = queries.size();
    int last = 0;
    for (int i = 0; i < n - 1; i++)
    {
        minTime += queries[i];
        last += minTime;
    }
    return last;
}

int main()
{
    vector<int> arr = {3, 2, 1, 2, 6};
    int x = minimumWaitingTime(arr);
    cout << x;
}