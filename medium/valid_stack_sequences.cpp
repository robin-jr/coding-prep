#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        vector<int> ref_stack;
        while (true){
            if (ref_stack.size()>0 and popped.size()>0 and ref_stack.back() ==popped[0]){
                ref_stack.pop_back();
                popped.erase(popped.begin());
            }else{
                if(pushed.size()<1){
                    break;
                }
                ref_stack.push_back(pushed[0]);
                pushed.erase(pushed.begin());
            }
        }
        return pushed.size()==0 and popped.size()==0;
    }
};

int main(){
    vector<int> pushed = {1,2,3,4,5}, popped = {4,5,3,2,1};
    // popped={4,3,5,1,2};
    Solution s = Solution();
    bool x= s.validateStackSequences(pushed, popped);
    cout<<x;
}
