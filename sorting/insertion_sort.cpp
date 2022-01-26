#include <iostream>
#include <string>

using namespace std;

void printArray(int arr[])
{
    for (int i = 0; i < 4; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int arr[] = {5, 9, 4, 3};
    int n = 4;
    for (int i = 0; i < n; i++)
    {
        int j = i;
        int t = arr[i];
        for (; j >= 0; j--)
        {
            if (arr[j] > t)
            {
                arr[j + 1] = arr[j];
            }
            else if (arr[j] < t)
            {
                break;
            }
        }
        arr[j + 1] = t;
    }

    printArray(arr);
}