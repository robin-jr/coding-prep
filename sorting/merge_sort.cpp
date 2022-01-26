#include <iostream>
#include <vector>
using namespace std;

class Merge
{
private:
    void merge(vector<int> a, vector<int> b, vector<int> *c)
    {
        int i = 0, j = 0, k = 0;
        while (i < a.size() && j < b.size())
        {
            if (a[i] < b[j])
            {
                (*c)[k++] = a[i++];
            }
            else
            {
                (*c)[k++] = b[j++];
            }
        }
        while (i < a.size())
        {
            (*c)[k++] = a[i++];
        }
        while (j < b.size())
        {
            (*c)[k++] = b[j++];
        }
    }

public:
    void print(vector<int> a)
    {
        for (auto &&i : a)
        {
            cout << i << " ";
        }
        cout << endl;
    }
    void mergeSort(vector<int> *a)
    {
        if ((*a).size() < 2)
        {
            return;
        }

        int m = (*a).size() / 2;
        vector<int> l;
        vector<int> r;

        for (int i = 0; i < m; i++)
        {
            l.push_back((*a)[i]);
        }
        for (int i = m; i < (*a).size(); i++)
        {
            r.push_back((*a)[i]);
        }

        mergeSort(&l);
        mergeSort(&r);

        merge(l, r, a);
    }
};
int main()
{
    Merge m = Merge();
    // vector<int> a = {3, 2, 1, 4, 0, 9};
    vector<int> a = {3, 2, 1, 4};
    m.mergeSort(&a);
    m.print(a);
}