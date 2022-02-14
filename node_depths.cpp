
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class BinaryTree {
public:
  int value;
  BinaryTree *left;
  BinaryTree *right;

  BinaryTree(int value) {
    this->value = value;
    left = nullptr;
    right = nullptr;
  }
};

int getSum(BinaryTree* root,int currentDepth){
    int sum=0;
    if(root==nullptr)
        return 0;
    sum += currentDepth;
    sum += getSum(root->left,currentDepth+1);
    sum += getSum(root->right,currentDepth+1);
    return sum;
}

int nodeDepths(BinaryTree *root) {
  return getSum(root,0);
}

int main(){
    
}