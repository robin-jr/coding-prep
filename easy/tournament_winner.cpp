#include <vector>
#include <bits/stdc++.h>

using namespace std;

string tournamentWinner(vector<vector<string>> competitions,
                        vector<int> results)
{
    int no_of_competitions = competitions.size();
    map<string, int> points  ;

    for (int i = 0; i < no_of_competitions; i++)
    {
        if (results[i] == 1)
        {
            // home team won
            points[competitions[i][0]] += 1;
        }
        else
        {
            // away team won
            points[competitions[i][1]] += 1;
        }
    }

    multimap<int, string> mm = {};
    for (auto &&it : points)
    {
        mm.insert({it.second, it.first});
    }

    string x= mm.rbegin()->second;
    return x;
}

int main()
{
    vector<vector<string>> a = {
        {"HTML", "C#"},
        {"C#", "Python"},
        {"Python", "HTML"}};
    vector<int> b = {0, 1, 0};
    string x = tournamentWinner(a, b);
    cout << x << endl;
}