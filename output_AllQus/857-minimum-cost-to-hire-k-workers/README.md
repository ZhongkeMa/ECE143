# [Minimum Cost to Hire K Workers][title]

## Description

There are `N` workers.  The `i`-th worker has a `quality[i]` and a minimum
wage expectation `wage[i]`.

Now we want to hire exactly `K` workers to form a _paid group_.   When hiring
a group of K workers, we must pay them according to the following rules:

  1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
  2. Every worker in the paid group must be paid at least their minimum wage expectation.

Return the least amount of money needed to form a paid group satisfying the
above conditions.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `1 <= K <= N <= 10000`, where `N = quality.length = wage.length`
  2. `1 <= quality[i] <= 10000`
  3. `1 <= wage[i] <= 10000`
  4. Answers within `10^-5` of the correct answer will be considered correct.


**Tags:** Heap

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/minimum-cost-to-hire-k-workers