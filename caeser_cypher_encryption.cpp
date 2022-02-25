#include <bits/stdc++.h>

using namespace std;
char getNewLetter(char letter, int key)
{
    int k = letter + key;
    return k <= 122 ? k : 96 + k % 122;
}
string caesarCypherEncryptor(string str, int key)
{
    key = key % 26;
    vector<char> s;
    for (int i = 0; i < str.size(); i++)
    {
        s.push_back(getNewLetter(str[i], key));
    }
    return string(s.begin(), s.end());
}

int main()
{
    string a = "xyz";
    string x = caesarCypherEncryptor(a, 2);
    cout << x;
}
