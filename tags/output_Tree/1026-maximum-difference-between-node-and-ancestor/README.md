# [Maximum Difference Between Node and Ancestor][title]

## Description

Given the `root` of a binary tree, find the maximum value `V` for which there
exists **different** nodes `A` and `B` where `V = |A.val - B.val|` and `A` is
an ancestor of `B`.

(A node A is an ancestor of B if either: any child of A is equal to B, or any
child of A is an ancestor of B.)



**Example 1:**

![](http://i68.tinypic.com/2whqcep.jpg)
        



**Note:**

  1. The number of nodes in the tree is between `2` and `5000`.
  2. Each node will have value between `0` and `100000`.


**Tags:** Tree, Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor