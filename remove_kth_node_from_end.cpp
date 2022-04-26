#include <bits/stdc++.h>

using namespace std;

class LinkedList {
public:
  int value;
  LinkedList *next;

  LinkedList(int value);
  void addMany(vector<int> values);
  vector<int> getNodesInArray();
};

void removeKthNodeFromEnd(LinkedList *head, int k) {
    LinkedList *t = head;
    int len=0;
    while (t!=nullptr) 
    {
        t = t->next;
        len++;
    }
    t = head;
    int distance = len - k;
    LinkedList *prev = nullptr;
    while (distance--)
    {
       prev = t; 
       t = t->next;
    }
    if (prev!=nullptr)
        prev->next = t->next;
    if (len==k && head->next!=nullptr){
        head->value = head->next->value;
        head->next=head->next->next;
    }
}
