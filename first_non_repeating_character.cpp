#include <bits/stdc++.h>

using namespace std;

int firstNonRepeatingCharacter(string string)
{
    map<char, int> characters_map = {};
    for (int i = 0; i < string.size(); i++)
    {
        characters_map[string[i]]=characters_map[string[i]]+1;
    }

    for (int i = 0; i < string.size(); i++)
    {
        if (characters_map[string[i]]==1)
        {
            return i;
        }
    }

    return -1;
}

int main()
{
    string a = "abcddfcaf";
    int x = firstNonRepeatingCharacter(a);
    cout << x << endl;
}
