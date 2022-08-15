#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string s = "a,b$c";
    int i = 0, j = s.length() - 1;
    char special_chars[] = {'@', '#', ',', '$'};
    while (i < j)
    {
        if (find(begin(special_chars), end(special_chars), s[i]) != end(special_chars))
        {
            i += 1;
        }
        else if (find(begin(special_chars), end(special_chars), s[j]) != end(special_chars))
        {
            j -= 1;
        }
        else
        {
            swap(s[i],s[j]);
            i += 1;
            j -= 1;
        }
    }
    cout << s;
}
