#include <bits/stdc++.h>

using namespace std;

vector<int> insertionSort(vector<int> array)
{
    int n = array.size();
    for (int i = 1; i < n; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (array[j] < array[j - 1])
            {
                swap(array[j], array[j - 1]);
            }else{
                break;
            }
        }
    }
    return array;
}

int main()
{
    vector<int> a = {8, 5, 2, 9, 5, 6, 3};
    vector<int> b = insertionSort(a);
    for (auto &&i : b)
    {
        cout << i << " ";
    }
}
