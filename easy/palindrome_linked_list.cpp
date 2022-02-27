#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;
//   Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        string a = "";
        ListNode *t = head;
        while (t)
        {
            a.append(to_string(t->val));
            t = t->next;
        }
        string b=a;
        reverse(a.begin(),a.end());
        return a==b;
    }
};

int main()
{
    Solution s = Solution();
    ListNode head = ListNode(1);
    ListNode p1 = ListNode(2);
    head.next = &p1;
    bool x = s.isPalindrome(&head);
    cout << x;
}