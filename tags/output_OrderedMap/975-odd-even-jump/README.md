# [Odd Even Jump][title]

## Description

You are given an integer array `A`.  From some starting index, you can make a
series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called _odd
numbered jumps_ , and the (2nd, 4th, 6th, ...) jumps in the series are called
_even numbered jumps_.

You may from index `i` jump forward to index `j` (with `i < j`) in the
following way:

  * During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that `A[i] <= A[j]` and `A[j]` is the smallest possible value.  If there are multiple such indexes `j`, you can only jump to the **smallest** such index ` j`.
  * During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that `A[i] >= A[j]` and `A[j]` is the largest possible value.  If there are multiple such indexes `j`, you can only jump to the **smallest** such index ` j`.
  * (It may be the case that for some index `i,` there are no legal jumps.)

A starting index is _good_ if, starting from that index, you can reach the end
of the array (index `A.length - 1`) by jumping some number of times (possibly
0 or more than once.)

Return the number of good starting indexes.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= A.length <= 20000`
  2. `0 <= A[i] < 100000`


**Tags:** Dynamic Programming, Stack, Ordered Map

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/odd-even-jump