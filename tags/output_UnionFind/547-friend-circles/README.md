# [Friend Circles][title]

## Description

There are **N** students in a class. Some of them are friends, while some are
not. Their friendship is transitive in nature. For example, if A is a
**direct** friend of B, and B is a **direct** friend of C, then A is an
**indirect** friend of C. And we defined a friend circle is a group of
students who are direct or indirect friends.

Given a **N*N** matrix **M** representing the friend relationship between
students in the class. If M[i][j] = 1, then the i th and jth students are
**direct** friends with each other, otherwise not. And you have to output the
total number of friend circles among all the students.

**Example 1:**  
        

**Example 2:**  
        

**Note:**  

  1. N is in range [1,200].
  2. M[i][i] = 1 for all students.
  3. If M[i][j] = 1, then M[j][i] = 1.


**Tags:** Depth-first Search, Union Find

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/friend-circles