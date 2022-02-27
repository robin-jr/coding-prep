#include <vector>
#include <bits/stdc++.h>

using namespace std;

class Node
{
public:
    string name;
    vector<Node *> children;

    Node(string str) { name = str; }

    void dfs(Node *root, vector<string> &array)
    {
        if (root==nullptr)  
        {
            return;
        }
        
        array.push_back(root->name);
        for (auto &&child : root->children)
        {
            dfs(child, array);
        }
    }

    vector<string> depthFirstSearch(vector<string> *array)
    {
        dfs(this, *array);
        return *array;
    }

    Node *addChild(string name)
    {
        Node *child = new Node(name);
        children.push_back(child);
        return this;
    }
};

int main()
{
}