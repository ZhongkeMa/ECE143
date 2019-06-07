# [K-th Smallest Prime Fraction][title]

## Description

A sorted list `A` contains 1, plus some number of primes.  Then, for every p <
q in the list, we consider the fraction p/q.

What is the `K`-th smallest fraction considered?  Return your answer as an
array of ints, where `answer[0] = p` and `answer[1] = q`.
        

**Note:**

  * `A` will have length between `2` and `2000`.
  * Each `A[i]` will be between `1` and `30000`.
  * `K` will be between `1` and `A.length * (A.length - 1) / 2`.


**Tags:** Binary Search, Heap

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/k-th-smallest-prime-fraction