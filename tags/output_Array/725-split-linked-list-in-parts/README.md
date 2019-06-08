# [Split Linked List in Parts][title]

## Description

Given a (singly) linked list with head node `root`, write a function to split
the linked list into `k` consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should
have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal parts
occurring later.

Return a List of ListNode's representing the linked list parts that are
formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

**Example 1:**  
        

**Example 2:**  
        

**Note:**

* The length of `root` will be in the range `[0, 1000]`.
* Each value of a node in the input will be an integer in the range `[0, 999]`.
* `k` will be an integer in the range `[1, 50]`.


**Tags:** Linked List

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/split-linked-list-in-parts