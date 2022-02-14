#include <vector>
#include <bits/stdc++.h>

using namespace std;

int nonConstructibleChange(vector<int> coins)
{
    int n = coins.size();
    if (n<1)
    {
        return 1;
    }
    
    sort(coins.begin(), coins.end());

    int change = 0;
    for (int i = 0; i < n; i++)
    {
        int current = coins[i];
        if (current > change + 1)
        {
            return change + 1;
        }
        change += current;
    }
    return change+1;
}

int main()
{
    vector<int> coins = {5, 7, 1, 1, 2, 3, 22};
    int x = nonConstructibleChange(coins);
    cout << x << "\n";
}