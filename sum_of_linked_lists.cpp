#include <bits/stdc++.h>

using namespace std;

// This is an input struct. Do not edit.
class LinkedList
{
public:
    int value;
    LinkedList *next = nullptr;

    LinkedList(int value) { this->value = value; }
};

LinkedList *sumOfLinkedLists(LinkedList *linkedListOne,
                             LinkedList *linkedListTwo)
{
    int carry = 0;
    LinkedList *t1 = linkedListOne;
    LinkedList *t2 = linkedListTwo;

    LinkedList *result = new LinkedList(0);
    LinkedList *r = result;
    while (t1 != nullptr || t2 != nullptr || carry != 0)
    {
        int sum =( t1 == nullptr ? 0 : t1->value) + (t2 == nullptr ? 0: t2->value) +carry;
        carry = sum/10;
        r->next =new LinkedList(sum%10);
        r=r->next;
        if (t1 != nullptr)
            t1 = t1->next;
        if (t2 != nullptr)
            t2 = t2->next;
    }
    return result->next;
}