
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class BinaryTree
{
public:
    int value;
    BinaryTree *left;
    BinaryTree *right;

    BinaryTree(int value)
    {
        this->value = value;
        left = nullptr;
        right = nullptr;
    }
};

void getSums(BinaryTree *root, vector<int> &sums, int sumUntil)
{
    if (root==nullptr)
    {
        return;
    }
    
    sumUntil += root->value;
    if (root->left == nullptr && root->right==nullptr)
    {
        sums.push_back(sumUntil);
        return;
    }

    getSums(root->left, sums, sumUntil);
    getSums(root->right, sums, sumUntil);
}

vector<int> branchSums(BinaryTree *root)
{
    vector<int> sums = {};
    int sumUntil = 0;

    getSums(root, sums, sumUntil);

    return sums;
}

int main()
{
}