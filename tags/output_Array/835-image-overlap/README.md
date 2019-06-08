# [Image Overlap][title]

## Description

Two images `A` and `B` are given, represented as binary, square matrices of
the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down
any number of units), and place it on top of the other image.  After, the
_overlap_ of this translation is the number of positions that have a 1 in both
images.

(Note also that a translation does **not** include any kind of rotation.)

What is the largest possible overlap?

**Example 1:**
        

**Notes:**  

  1. `1 <= A.length = A[0].length = B.length = B[0].length <= 30`
  2. `0 <= A[i][j], B[i][j] <= 1`


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/image-overlap