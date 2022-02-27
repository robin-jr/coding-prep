#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence)
{
    int i = 0, j = 0; // two pointers
    int n1 = array.size();
    int n2 = sequence.size();

    while (i < n1 && j < n2)
    {
        if (sequence[j] == array[i])
        {
            // They are equal. increment both pointers
            j += 1;
            i += 1;
        }
        else
        {
            i += 1;
            // increment pointer-1
        }
    }
    if (j >= n2)
    {
        // j (pointer-2) has reached the end of the sequence
        return true;
    }

    return false;
}

int main()
{
    vector<int> a = {5, 1, 22, 25, 6, -1, 8, 10};
    vector<int> seq = {1, 6, -1};
    bool x = isValidSubsequence(a, seq);
    cout << x;
}