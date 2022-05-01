#include <bits/stdc++.h>

using namespace std;

class LinkedList
{
public:
    int value;
    LinkedList *next;

    LinkedList(int value);
    void addMany(vector<int> values);
    vector<int> getNodesInArray();
};

void removeKthNodeFromEnd(LinkedList *head, int k)
{
    LinkedList *first = head;
    LinkedList *second = head;

    while (k--)
        second = second->next;

    if (second == nullptr)
    {
        head->value = head->next->value;
        head->next = head->next->next;
        return;
    }

    LinkedList *prev = nullptr;
    while (second != nullptr)
    {
        prev = first;
        first = first->next;
        second = second->next;
    }
    prev->next = first->next;
}
