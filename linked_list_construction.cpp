#include <bits/stdc++.h>

using namespace std;

class Node
{
public:
    int value;
    Node *prev;
    Node *next;

    Node(int value);
};

// Feel free to add new properties and methods to the class.
class DoublyLinkedList
{
private:
    void removeNodeBindings(Node *node)
    {
        if (node->prev != nullptr)
            node->prev->next = node->next;
        if (node->next != nullptr)
            node->next->prev = node->prev;
        node->next = nullptr;
        node->prev = nullptr;
    }

public:
    Node *head;
    Node *tail;

    DoublyLinkedList()
    {
        head = nullptr;
        tail = nullptr;
    }

    void setHead(Node *node)
    {
        if (head == nullptr)
            head = tail = node;
        else
            insertBefore(head, node);
    }

    void setTail(Node *node)
    {
        if (tail == nullptr)
            setHead(node);
        else
            insertAfter(tail, node);
    }

    void insertBefore(Node *node, Node *nodeToInsert)
    {
        if (nodeToInsert == head && nodeToInsert == tail)
            return;
        remove(nodeToInsert);
        nodeToInsert->next = node;
        nodeToInsert->prev = node->prev;
        if (node->prev == nullptr)
            head = nodeToInsert;
        else
            node->prev->next = nodeToInsert;
        node->prev = nodeToInsert;
    }

    void insertAfter(Node *node, Node *nodeToInsert)
    {
        if (nodeToInsert == head && nodeToInsert == tail)
            return;
        remove(nodeToInsert);
        nodeToInsert->prev = node;
        nodeToInsert->next = node->next;
        if (node->next == nullptr)
            tail = nodeToInsert;
        else
            node->next->prev = nodeToInsert;
        node->next = nodeToInsert;
    }

    void insertAtPosition(int position, Node *nodeToInsert)
    {
        if (position == 1)
            return setHead(nodeToInsert);
        Node *t = head;
        int p = 1;
        while (t != nullptr && p++ < position)
            t = t->next;
        if (t == nullptr)
            return setTail(nodeToInsert);
        insertBefore(t, nodeToInsert);
    }

    void removeNodesWithValue(int value)
    {
        Node *t = head;
        while (t != NULL)
        {
            if (t->value == value)
            {
                Node *next = t->next;
                remove(t);
                t = next;
                continue;
            }
            t = t->next;
        }
    }

    void remove(Node *node)
    {
        if (node == head)
            head = node->next;
        if (node == tail)
            tail = node->prev;

        removeNodeBindings(node);
    }

    bool containsNodeWithValue(int value)
    {
        Node *t = head;
        while (t != NULL && t->value != value)
        {
            t = t->next;
        }
        return t != NULL && t->value == value;
    }
};
