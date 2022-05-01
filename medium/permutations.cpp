#include <bits/stdc++.h>

using namespace std;

void helper(vector<int> array, vector<int> prefix, vector<vector<int>> &r)
{
    int n = array.size();
    if (n == 0)
        r.push_back(prefix);
    for (int i = 0; i < n; i++)
    {
        vector<int> temp = array;
        temp.erase(temp.begin() + i);
        vector<int> t2 = prefix;
        t2.push_back(array[i]);
        helper(temp, t2, r);
    }
}
vector<vector<int>> getPermutations(vector<int> array)
{
    vector<vector<int>> r = {};
    if (array.size() == 0)
        return {};

    helper(array, {}, r);
    return r;
}

int main()
{
    auto x = getPermutations({1, 2, 3});
    for (auto &&i : x)
    {
        for (auto &&a : i)
        {
            cout << a << " ";
        }
        cout << "-" << endl;
    }
}