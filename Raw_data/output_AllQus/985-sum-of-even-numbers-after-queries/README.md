# [Sum of Even Numbers After Queries][title]

## Description

We have an array `A` of integers, and an array `queries` of queries.

For the `i`-th query `val = queries[i][0], index = queries[i][1]`, we add val
to `A[index]`.  Then, the answer to the `i`-th query is the sum of the even
values of `A`.

_(Here, the given`index = queries[i][1]` is a 0-based index, and each query
permanently modifies the array `A`.)_

Return the answer to all queries.  Your `answer` array should have `answer[i]`
as the answer to the `i`-th query.



**Example 1:**
        



**Note:**

  1. `1 <= A.length <= 10000`
  2. `-10000 <= A[i] <= 10000`
  3. `1 <= queries.length <= 10000`
  4. `-10000 <= queries[i][0] <= 10000`
  5. `0 <= queries[i][1] < A.length`


**Tags:** Array

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/sum-of-even-numbers-after-queries