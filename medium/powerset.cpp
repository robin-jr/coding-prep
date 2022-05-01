#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> helper(vector<int> array, int idx)
{
    if (idx < 0)
        return {{}};
    int ele = array[idx];
    vector<vector<int>> subsets = helper(array, idx - 1);
    int len=subsets.size();
    for (int i = 0; i < len; i++)
    {
        vector<int> currentSubset = subsets[i];
        currentSubset.push_back(ele);
        subsets.push_back(currentSubset);
    }
    return subsets;
}

vector<vector<int>> powerset(vector<int> array)
{
    // return helper(array, array.size() - 1);
    vector<vector<int>> set = {{}};

    for (int e : array)
    {
        vector<vector<int>> newSubset = {};
        for (vector<int> f : set)
        {
            f.push_back(e);
            newSubset.push_back(f);
        }
        set.insert(set.end(), newSubset.begin(), newSubset.end());
    }

    return set;
}


int main()
{
    auto x = powerset({1, 2, 3});
    for (auto &&i : x)
    {
        for (auto &&a : i)
        {
            cout << a << " ";
        }
        cout << "-" << endl;
    }
}