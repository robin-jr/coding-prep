#include <bits/stdc++.h>
#include <any>
#include <vector>

using namespace std;

int getSum(vector<any> array, int depth)
{
    int sum = 0;
    for (int i = 0; i < array.size(); i++)
    {
        any el = array[i];
        if (el.type() == typeid(vector<any>))
        {
            sum += (depth + 1) * getSum(any_cast<vector<any>>(el), depth + 1);
        }
        else
        {
            sum += any_cast<int>(el);
        }
    }
    return sum;
}

int productSum(vector<any> array)
{
    return getSum(array, 1);
}

int main()
{
}