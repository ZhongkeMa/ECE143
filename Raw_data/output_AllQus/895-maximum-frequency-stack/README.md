# [Maximum Frequency Stack][title]

## Description

Implement `FreqStack`, a class which simulates the operation of a stack-like
data structure.

`FreqStack` has two functions:

  * `push(int x)`, which pushes an integer `x` onto the stack.
  * `pop()`, which **removes** and returns the most frequent element in the stack.     * If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.



**Example 1:**
        



**Note:**

  * Calls to `FreqStack.push(int x)` will be such that `0 <= x <= 10^9`.
  * It is guaranteed that `FreqStack.pop()` won't be called if the stack has zero elements.
  * The total number of `FreqStack.push` calls will not exceed `10000` in a single test case.
  * The total number of `FreqStack.pop` calls will not exceed `10000` in a single test case.
  * The total number of `FreqStack.push` and `FreqStack.pop` calls will not exceed `150000` across all test cases.




**Tags:** Hash Table, Stack

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/maximum-frequency-stack