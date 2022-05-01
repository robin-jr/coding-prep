#include <bits/stdc++.h>

using namespace std;

class MyHashMap
{
    int size = 1000;
    vector<vector<vector<int>>> a;

private:
    int getHash(int key)
    {
        int hash = key % size;
        return hash;
    }

    int getIdx(int hash, int key)
    {
        for (int i = 0; i < a[hash].size(); i++)
        {
            if (a[hash][i][0] == key)
            {
                return i;
            }
        }
        return -1;
    }

public:
    MyHashMap()
    {
        a.resize(size);
    }

    void put(int key, int value)
    {
        int hash = getHash(key);
        int idx = getIdx(hash, key);
        if (idx == -1)
            a[hash].push_back({key, value});
        else
            a[hash][idx] = {key, value};
    }

    int get(int key)
    {
        int hash = getHash(key);
        int idx = getIdx(hash, key);
        if (idx != -1)
            return a[hash][idx][1];
        return -1;
    }

    void remove(int key)
    {
        int hash = getHash(key);
        int idx = getIdx(hash, key);
        if (idx != -1)
            a[hash].erase(a[hash].begin() + idx);
    }
};

int main()
{
    MyHashMap *obj = new MyHashMap();
    int key = 1;
    int value = 11;
    obj->put(key, value);
    int param_2 = obj->get(key);
    printf("param2 %d", param_2);
    obj->remove(key);
    param_2 = obj->get(key);
    printf("param2 %d", param_2);
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */