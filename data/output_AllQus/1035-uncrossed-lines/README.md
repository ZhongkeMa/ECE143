# [Uncrossed Lines][title]

## Description

We write the integers of `A` and `B` (in the order they are given) on two
separate horizontal lines.

Now, we may draw _connecting lines_ : a straight line connecting two numbers
`A[i]` and `B[j]` such that:

  * `A[i] == B[j]`;
  * The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each
number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.



**Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/26/142.png)
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= A.length <= 500`
  2. `1 <= B.length <= 500`
  3. ` 1 <= A[i], B[i] <= 2000`


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/uncrossed-lines