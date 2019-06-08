# [Recover a Tree From Preorder Traversal][title]

## Description

We run a preorder depth first search on the `root` of a binary tree.

At each node in this traversal, we output `D` dashes (where `D` is the _depth_
of this node), then we output the value of this node.    _(If the depth of a
node is`D`, the depth of its immediate child is `D+1`.  The depth of the root
node is `0`.)_

If a node has only one child, that child is guaranteed to be the left child.

Given the output `S` of this traversal, recover the tree and return its
`root`.



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/04/08/recover-a-tree-from-
preorder-traversal.png)**
        

**Example 2:**

**![](https://assets.leetcode.com/uploads/2019/04/11/screen-
shot-2019-04-10-at-114101-pm.png)**
        



**Example 3:**

![](https://assets.leetcode.com/uploads/2019/04/11/screen-
shot-2019-04-10-at-114955-pm.png)
        



**Note:**

  * The number of nodes in the original tree is between `1` and `1000`.
  * Each node will have a value between `1` and `10^9`.


**Tags:** Tree, Depth-first Search

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal