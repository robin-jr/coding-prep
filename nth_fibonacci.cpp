#include <bits/stdc++.h>

using namespace std;

int getNthFib(int n)
{
    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 0;
    }
    int a = 0, b = 1;
    int i = 0;
    while (i < n-2 )
    {
        int t = b;
        b = a + b;
        a = t;
        i += 1;
    }
    return b;
}

int main()
{
    for (int i = 1; i < 10; i++)
    {
        int x = getNthFib(i);
        cout << x << " ";
    }
}