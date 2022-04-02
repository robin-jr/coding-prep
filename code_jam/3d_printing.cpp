#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    int test_case;
    int x;
    for (test_case = 0; test_case < T; test_case++)
    {
        vector<vector<int>> p;
        for (int i = 0; i < 3; i++)
        {
            p.push_back({});
            for (int j = 0; j < 4; j++)
            {
                cin >> x;
                p[i].push_back(x);
            }
        }
        int c, m, y, k;
        c = min(min(p[0][0], p[1][0]), p[2][0]);
        m = min(min(p[0][1], p[1][1]), p[2][1]);
        y = min(min(p[0][2], p[1][2]), p[2][2]);
        k = min(min(p[0][3], p[1][3]), p[2][3]);
        cout << "Case #" << test_case + 1 << ": ";
        int sum = c + m + y + k;
        if (sum < 10e5)
        {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        int diff = sum - 10e5;
        while (diff > 0)
        {
            if (k >= diff)
            {
                k -= diff;
                diff = 0;
            }
            else if (y >= diff)
            {
                y -= diff;
                diff = 0;
            }
            else if (m >= diff)
            {
                m -= diff;
                diff = 0;
            }
            else if (c >= diff)
            {
                c -= diff;
                diff = 0;
            }
            else if (diff > k)
            {
                diff -= k;
                k = 0;
            }
            else if (diff > y)
            {
                diff -= y;
                y = 0;
            }
            else if (diff > m)
            {
                diff -= m;
                m = 0;
            }
            else if (diff > c)
            {
                diff -= c;
                c = 0;
            }
        }
        cout << c << " " << m << " " << y << " " << k << "\n";
    }
}
