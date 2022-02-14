
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class BST
{
public:
    int value;
    BST *left;
    BST *right;

    BST(int val);
    BST &insert(int val);
};

int findClosestValueInBst(BST *tree, int target)
{
    BST *current = tree;
    BST *minNode = current;
    while (current != nullptr)
    {
        if (abs(target - current->value) < abs(target - minNode->value))
        {
            minNode = current;
        }
        if (current->value < target)
        {
            current = current->right;
        }
        else
        {
            current = current->left;
        }
    }

    return minNode->value;
}

int main()
{
}