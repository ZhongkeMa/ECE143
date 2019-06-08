# [Possible Bipartition][title]

## Description

Given a set of `N` people (numbered `1, 2, ..., N`), we would like to split
everyone into two groups of **any** size.

Each person may dislike some other people, and they should not go into the
same group.

Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the
people numbered `a` and `b` into the same group.

Return `true` if and only if it is possible to split everyone into two groups
in this way.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= N <= 2000`
  2. `0 <= dislikes.length <= 10000`
  3. `1 <= dislikes[i][j] <= N`
  4. `dislikes[i][0] < dislikes[i][1]`
  5. There does not exist `i != j` for which `dislikes[i] == dislikes[j]`.


**Tags:** Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/possible-bipartition