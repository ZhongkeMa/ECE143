# [Circular Array Loop][title]

## Description

You are given a **circular** array `nums` of positive and negative integers.
If a number _k_ at an index is positive, then move forward _k_ steps.
Conversely, if it 's negative (- _k_ ), move backward _k_  steps. Since the
array is circular, you may assume that the last element's next element is the
first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in `nums`. A cycle must start and
end at the same index and the cycle's length > 1\. Furthermore, movements in a
cycle must all follow a single direction. In other words, a cycle must not
consist of both forward and backward movements.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. -1000 ≤ nums[i] ≤ 1000
  2. nums[i] ≠ 0
  3. 1 ≤ nums.length ≤ 5000



**Follow up:**

Could you solve it in **O(n)** time complexity and   **O(1)** extra space
complexity?


**Tags:** Array, Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/circular-array-loop