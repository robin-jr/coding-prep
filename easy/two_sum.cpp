#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    map<int, int> d = {};
    vector<int> result = {};

    int n = array.size();
    for (int i = 0; i < n; i++)
    {
        if (d.find(array[i]) == d.end())
        {
            // element not found.
            d[targetSum - array[i]] = array[i];
        }
        else
        {
            result.push_back(array[i]);
            result.push_back(d[array[i]]);
        }
    }

    return result;
}

void printVector(vector<int> arr)
{
    for (auto &&e : arr)
    {
        cout << e << " ";
    }
    cout << endl;
}
int main()
{
    vector<int> array = {3, 5, -4, 8, 11, 1, -1, 6};
    vector<int> x = twoNumberSum(array, 10);
    printVector(x);
}