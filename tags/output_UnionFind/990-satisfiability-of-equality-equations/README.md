# [Satisfiability of Equality Equations][title]

## Description

Given an array equations of strings that represent relationships between
variables, each string `equations[i]` has length `4` and takes one of two
different forms: `"a==b"` or `"a!=b"`.  Here, `a` and `b` are lowercase
letters (not necessarily different) that represent one-letter variable names.

Return `true` if and only if it is possible to assign integers to variable
names so as to satisfy all the given equations.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        



**Note:**

  1. `1 <= equations.length <= 500`
  2. `equations[i].length == 4`
  3. `equations[i][0]` and `equations[i][3]` are lowercase letters
  4. `equations[i][1]` is either `'='` or `'!'`
  5. `equations[i][2]` is `'='`


**Tags:** Union Find, Graph

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/satisfiability-of-equality-equations