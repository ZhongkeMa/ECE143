# [Open the Lock][title]

## Description

You have a lock in front of you with 4 circular wheels. Each wheel has 10
slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can
rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or
`'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the
4 wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any
of these codes, the wheels of the lock will stop turning and you will be
unable to open it.

Given a `target` representing the value of the wheels that will unlock the
lock, return the minimum total number of turns required to open the lock, or
-1 if it is impossible.

**Example 1:**  
        

**Example 2:**  
        

**Example 3:**  
        

**Example 4:**  
        

**Note:**  

  1. The length of `deadends` will be in the range `[1, 500]`.
  2. `target` will not be in the list `deadends`.
  3. Every string in `deadends` and the string `target` will be a string of 4 digits from the 10,000 possibilities `'0000'` to `'9999'`.


**Tags:** Breadth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/open-the-lock