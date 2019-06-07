# [Smallest String Starting From Leaf][title]

## Description

Given the `root` of a binary tree, each node has a value from `0` to `25`
representing the letters `'a'` to `'z'`: a value of `0` represents `'a'`, a
value of `1` represents `'b'`, and so on.

Find the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

_(As a reminder, any shorter prefix of a string is lexicographically smaller:
for example,`"ab"` is lexicographically smaller than `"aba"`.  A leaf of a
node is a node that has no children.)_



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/01/30/tree1.png)**
        

**Example 2:**

**![](https://assets.leetcode.com/uploads/2019/01/30/tree2.png)**
        

**Example 3:**

**![](https://assets.leetcode.com/uploads/2019/02/01/tree3.png)**
        



**Note:**

  1. The number of nodes in the given tree will be between `1` and `8500`.
  2. Each node in the tree will have a value between `0` and `25`.


**Tags:** Tree, Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/smallest-string-starting-from-leaf