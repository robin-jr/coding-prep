#include <string>
#include <iostream>
#include <sstream> 
#include <bits/stdc++.h>
// #include <vector>

using namespace std;
int max_gold=0;

void hit(vector<vector<int> > arr, int pointsSoFar, bool isAsha,int p,int q)
{
    if (arr.size() < 1)
    {
        max_gold = max(max_gold, pointsSoFar);
        return;
    }

    vector<vector<int> > a = arr;
    a[0][0] -= q;
    if (a[0][0] < 1)
    {
        a.erase(a.begin());
    }
    hit(a, pointsSoFar, true,p,q);

    if (isAsha)
    {
        for (int i = 0; i < arr.size(); i++)
        {
            vector<vector<int> > a = arr;
            a[i][0] -= p;
            int t = pointsSoFar;
            if (a[i][0] < 1)
            {
                t += a[i][1];
                a.erase(a.begin()+i);
            }
            hit(a, t, false,p,q);
        }
    }
}

int main()
{
    int p,q,n;
    cin>>p>>q>>n;
    max_gold=0;
    vector<vector<int> > arr( n , vector<int> (2, 0));
    
    for(int i=0;i<n;i++){
        int hp,score;
        cin>>hp>>score;
        arr[i][0]=hp;
        arr[i][1]=score;
    };
    // for (int i=0;i<n;i++){
    //     cout<<arr[i][0]<<" "<<arr[i][1]<<"\n";
    // };
    hit(arr,0,true,p,q);
    cout<<max_gold;
    return 0;
}
