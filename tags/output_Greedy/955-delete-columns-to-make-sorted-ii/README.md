# [Delete Columns to Make Sorted II][title]

## Description

We are given an array `A` of `N` lowercase letter strings, all of the same
length.

Now, we may choose any set of deletion indices, and for each string, we delete
all the characters in those indices.

For example, if we have an array `A = ["abcdef","uvwxyz"]` and deletion
indices `{0, 2, 3}`, then the final array after deletions is `["bef","vyz"]`.

Suppose we chose a set of deletion indices `D` such that after deletions, the
final array has its elements in **lexicographic** order (`A[0] <= A[1] <= A[2]
... <= A[A.length - 1]`).

Return the minimum possible value of `D.length`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= A.length <= 100`
  2. `1 <= A[i].length <= 100`


**Tags:** Greedy

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/delete-columns-to-make-sorted-ii