#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//   Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution
{
private:
    void dfs(TreeNode *root, vector<int> &a)
    {
        if (root == nullptr)
        {
            return;
        }

        dfs(root->left, a);
        a.push_back(root->val);
        dfs(root->right, a);
    }

public:
    vector<int> getAllElements(TreeNode *root1, TreeNode *root2)
    {
        vector<int> a, b;
        dfs(root1, a);
        dfs(root2, b);
        a.insert(a.begin(), b.begin(), b.end());
        sort(a.begin(), a.end());
        return a;
    }
    void print(vector<int> &a)
    {
        for (auto &&i : a)
        {
            cout << i << " ";
        }
        cout << endl;
    }
};

int main()
{
    TreeNode r1 = TreeNode(1);
    TreeNode a1 = TreeNode(2);
    r1.left = &a1;
    TreeNode r2 = TreeNode(11);
    TreeNode a2 = TreeNode(12);
    r2.left = &a2;

    Solution s = Solution();
    vector<int> r = s.getAllElements(&r1, &r2);
    s.print(r);
}