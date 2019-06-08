# [Minimum Swaps To Make Sequences Increasing][title]

## Description

We have two integer sequences `A` and `B` of the same non-zero length.

We are allowed to swap elements `A[i]` and `B[i]`.  Note that both elements
are in the same index position in their respective sequences.

At the end of some number of swaps, `A` and `B` are both strictly increasing.
(A sequence is _strictly increasing_ if and only if `A[0] < A[1] < A[2] < ...
< A[A.length - 1]`.)

Given A and B, return the minimum number of swaps to make both sequences
strictly increasing.  It is guaranteed that the given input always makes it
possible.
        

**Note:**

  * `A, B` are arrays with the same length, and that length will be in the range `[1, 1000]`.
  * `A[i], B[i]` are integer values in the range `[0, 2000]`.


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing