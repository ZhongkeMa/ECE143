# [Add Two Numbers][title]

## Description

You are given two **non-empty** linked lists representing two non-negative
integers. The digits are stored in **reverse order** and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

**Example:**
            Input: (2 - > 4 -> 3) + (5 -> 6 -> 4)    Output: 7 - > 0 -> 8    Explanation: 342 + 465 = 807.    


**Tags:** Linked List, Math

**Difficulty:** Medium

## 思路

``` cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        int rem = 0;
        while(l1 || l2) {
            int val1 = l1?l1->val:0;
            int val2 = l2?l2->val:0;
            int temp = val1 + val2 + rem;
            rem = temp/10;
            int add = temp%10;
            ListNode* node = new ListNode(add);
            curr->next = node;
            curr = curr->next;
            l1 = l1?l1->next:NULL;
            l2 = l2?l2->next:NULL;
        }
        if(l1 == NULL && l2 == NULL && rem == 1)
            curr->next = new ListNode(1);
        return head->next;
    }
};
```

[title]: https://leetcode.com/problems/add-two-numbers
