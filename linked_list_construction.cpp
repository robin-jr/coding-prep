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
        node->prev->next=node->next;
        node->next->prev=node->prev;
        node->next=head;
        head->prev=node;
        node->prev=nullptr;
        head=node;
    }

    void setTail(Node *node)
    {
        node->prev->next=node->next;
        node->next->prev=node->prev;
        node->prev=tail;
        tail->next=node;
        node->next=nullptr;
        tail=node;
    }

    void insertBefore(Node *node, Node *nodeToInsert)
    {
        Node* t=nodeToInsert;
        while(t!=nullptr){
            t=t->next;
        }
        t->next=node;
        nodeToInsert->prev=node->prev;
        node->prev->next=nodeToInsert;
        node->prev=t;
    }
                                                           
    void insertAfter(Node *node, Node *nodeToInsert)
    {
        Node* t=nodeToInsert;
        while(t!=nullptr){
            t=t->next;
        }
        t->next=node->next;
        nodeToInsert->prev=node->prev;
        node->next->prev=t;
        node->next=nodeToInsert;
    }

    void insertAtPosition(int position, Node *nodeToInsert)
    {
        Node* current = head;
        int i = 1;
        while (i<position)
        {
            i+=1;
            current=current->next;
        }
        insertBefore(current,nodeToInsert);
    }

    void removeNodesWithValue(int value)
    {
        Node *current = head;
        while (current != nullptr)
        {
            if (current->value == value)
            {
                current->prev->next = current->next;
                continue;
            }
            current = current->next;
        }
    }

    void remove(Node *node)
    {
        Node *current = head;
        while (current != nullptr)
        {
            if (current->value == node->value)
            {
                current->prev->next = current->next;
                break;
            }
            current = current->next;
        }
    }

    bool containsNodeWithValue(int value)
    {
        Node *current = head;
        while (current != nullptr)
        {
            if (current->value == value)
            {
                return true;
            }
            current = current->next;
        }
        return false;
    }
};
