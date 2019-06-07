# [Reverse Linked List][title]

## Description

Reverse a singly linked list.

**Example:**
        

**Follow up:**

A linked list can be reversed either iteratively or recursively. Could you
implement both?


**Tags:** Linked List

**Difficulty:** Easy

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
    ListNode* temp;
    
    void rec(ListNode* node)
    {
        if(node == NULL)
            return;
        
        if(node->next == NULL)
        {
            temp = node;
            return;
        }
        
        ListNode* t = node->next;
        rec(node->next);
        t->next = node;
        node->next = NULL;
    }
    ListNode* reverseList(ListNode* head) {
        temp = NULL;
        rec(head);
        return temp;
    }
};
```

[title]: https://leetcode.com/problems/reverse-linked-list