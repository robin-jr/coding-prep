#include <bits/stdc++.h>

using namespace std;

vector<int> selectionSort(vector<int> array)
{
    int minIdx;
    int n = array.size();
    for (int i = 0; i < n; i++)
    {
        minIdx=i;
        for (int j = i; j < n; j++)
        {
            if (array[j] < array[minIdx])
            {
                minIdx = j;
            }
        }
        swap(array[minIdx], array[i]);
    }
    return array;
}

int main()
{
    vector<int> a = {8, 5, 2, 9, 5, 6, 3};
    vector<int> b = selectionSort(a);
    for (auto &&i : b)
    {
        cout << i << " ";
    }
}
