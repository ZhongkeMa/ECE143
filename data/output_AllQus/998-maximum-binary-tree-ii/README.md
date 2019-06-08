# [Maximum Binary Tree II][title]

## Description

We are given the `root` node of a _maximum tree:_ a tree where every node has
a value greater than any other value in its subtree.

Just as in the [previous problem](https://leetcode.com/problems/maximum-
binary-tree/), the given tree was constructed from an list `A` (`root =
Construct(A)`) recursively with the following `Construct(A)` routine:

  * If `A` is empty, return `null`.
  * Otherwise, let `A[i]` be the largest element of `A`.  Create a `root` node with value `A[i]`.
  * The left child of `root` will be `Construct([A[0], A[1], ..., A[i-1]])`
  * The right child of `root` will be `Construct([A[i+1], A[i+2], ..., A[A.length - 1]])`
  * Return `root`.

Note that we were not given A directly, only a root node `root =
Construct(A)`.

Suppose `B` is a copy of `A` with the value `val` appended to it.  It is
guaranteed that `B` has unique values.

Return `Construct(B)`.



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-
tree-1-1.png)![](https://assets.leetcode.com/uploads/2019/02/21/maximum-
binary-tree-1-2.png)**
        

**Example 2:  
![](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-
tree-2-1.png)![](https://assets.leetcode.com/uploads/2019/02/21/maximum-
binary-tree-2-2.png)**
        

**Example 3:  
![](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-
tree-3-1.png)![](https://assets.leetcode.com/uploads/2019/02/21/maximum-
binary-tree-3-2.png)**
        



**Note:**

  1. `1 <= B.length <= 100`


**Tags:** Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/maximum-binary-tree-ii