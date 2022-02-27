#include <bits/stdc++.h>

using namespace std;

class LinkedList
{
public:
    int value;
    LinkedList *next = nullptr;

    LinkedList(int value) { this->value = value; }
};

LinkedList *removeDuplicatesFromLinkedList(LinkedList *linkedList)
{
    LinkedList *current = linkedList;
    LinkedList *previous = nullptr;

    while (current != nullptr)
    {
        if (previous != nullptr && current->value == previous->value)
        {
            previous->next = current->next;
            current = current->next;
            continue;
        }
        previous = current;
        current = current->next;
    }
    return linkedList;
}

int main()
{
}
