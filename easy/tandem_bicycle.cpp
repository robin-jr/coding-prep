#include <bits/stdc++.h>

using namespace std;

int tandemBicycle(vector<int> redShirtSpeeds, vector<int> blueShirtSpeeds,
                  bool fastest)
{
    sort(redShirtSpeeds.begin(), redShirtSpeeds.end());
    sort(blueShirtSpeeds.begin(), blueShirtSpeeds.end());

    int n = redShirtSpeeds.size();
    int sum = 0;

    for (int i = 0; i < n; i++)
    {
        if (fastest)
        {
            sum += max(redShirtSpeeds[i], blueShirtSpeeds[n-i-1]);
        }
        else
        {
            sum += max(redShirtSpeeds[i], blueShirtSpeeds[i]);
        }
    }
    return sum;
}

int main()
{
    vector<int> a = {5, 5, 3, 9, 2};
    vector<int> b = {3, 6, 7, 2, 1};

    int x = tandemBicycle(a,b,true);
    cout<<x;
}