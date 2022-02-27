#include <bits/stdc++.h>

using namespace std;

vector<int> bubbleSort(vector<int> array)
{
    int n = array.size();
    bool isSorted = false;
    int k = 0;
    while (!isSorted)
    {
        isSorted = true;
        for (int j = 0; j < n - 1 - k; j++)
        {
            if (array[j] > array[j + 1])
            {
                swap(array[j], array[j + 1]);
                isSorted = false;
            }
        }
    }
    return array;
}

int main()
{
    vector<int> a = {8, 5, 2, 9, 5, 6, 3};
    vector<int> b = bubbleSort(a);
    for (auto &&i : b)
    {
        cout << i << " ";
    }
}