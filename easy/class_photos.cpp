
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool classPhotos(vector<int> redShirtHeights, vector<int> blueShirtHeights)
{
    sort(redShirtHeights.begin(), redShirtHeights.end());
    sort(blueShirtHeights.begin(), blueShirtHeights.end());

    int flag = 0;
    for (int i = 0; i < redShirtHeights.size(); i++)
    {
        int diff = redShirtHeights[i] - blueShirtHeights[i];
        if (diff==0)
        {
            return false;
        }
        
        if (flag == 0)
        {
            if (diff < 0)
            {
                flag = -1;
            }
            else if (diff > 0)
            {
                flag = 1;
            }
        }
        if (flag < 0 && diff > 0)
        {
            return false;
        }
        if (flag > 0 && diff < 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    vector<int> a ={5, 8, 1, 3, 4};
    vector<int> b ={6, 9, 2, 4, 5};
    bool x=classPhotos(a,b);
    cout<<x;
}