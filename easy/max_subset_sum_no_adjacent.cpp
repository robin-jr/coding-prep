#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int maxSubsetSumNoAdjacent(vector<int> array)
{
    int n = array.size();
    if (n < 1)
    {
        return 0;
    }
    if (n == 1)
    {
        return array[0];
    }
    int maxSums[n]={array[0]};
    maxSums[1]=max(array[1],array[0]);
    for (int i = 2; i < n; i++)
    {
        maxSums[i]=max(maxSums[i-2]+array[i],maxSums[i-1]);
    }
    return maxSums[n-1];
}
int main()
{
    vector<int> a = {75, 105, 120, 75, 90, 135};
    int x = maxSubsetSumNoAdjacent(a);
    cout << x;
}