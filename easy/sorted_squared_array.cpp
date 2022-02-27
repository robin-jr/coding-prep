#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> sortedSquaredArray(vector<int> array)
{
    vector<int> result = {};
    int n = array.size();
    int lIdx = 0, rIdx = n - 1;

    while (lIdx <= rIdx)
    {
        int lElement=array[lIdx];
        int rElement=array[rIdx];

        if (abs(rElement)>abs(lElement)){
            result.insert(result.begin(),rElement*rElement);
            rIdx-=1;
        }else{
            result.insert(result.begin(),lElement*lElement);
            lIdx+=1;
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
    vector<int> arr = {-4,1, 2, 3, 5, 6, 8, 9};
    vector<int> x = sortedSquaredArray(arr);
    printVector(x);
}