# [Smallest Range][title]

## Description

You have `k` lists of sorted integers in ascending order. Find the
**smallest** range that includes at least one number from each of the `k`
lists.

We define the range [a,b] is smaller than range [c,d] if `b-a < d-c` or `a <
c` if `b-a == d-c`.

**Example 1:**  
        

**Note:**  

  1. The given list may contain duplicates, so ascending order means >= here.
  2. 1 <= `k` <= 3500
  3. -105 <= `value of elements` <= 105.
  4. **For Java users, please note that the input type has been changed to List <List<Integer>>. And after you reset the code template, you'll see this point.**

  


**Tags:** Hash Table, Two Pointers, String

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/smallest-range