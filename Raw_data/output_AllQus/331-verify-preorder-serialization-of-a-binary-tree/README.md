# [Verify Preorder Serialization of a Binary Tree][title]

## Description

One way to serialize a binary tree is to use pre-order traversal. When we
encounter a non-null node, we record the node's value. If it is a null node,
we record using a sentinel value such as `#`.
        

For example, the above binary tree can be serialized to the string
`"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `#` represents a null node.

Given a string of comma separated values, verify whether it is a correct
preorder traversal serialization of a binary tree. Find an algorithm without
reconstructing the tree.

Each comma separated value in the string must be either an integer or a
character `'#'` representing `null` pointer.

You may assume that the input format is always valid, for example it could
never contain two consecutive commas such as `"1,,3"`.

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        


**Tags:** Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree