# [Time Based Key-Value Store][title]

## Description

Create a timebased key-value store class `TimeMap`, that supports two
operations.

1\. `set(string key, string value, int timestamp)`

  * Stores the `key` and `value`, along with the given `timestamp`.

2\. `get(string key, int timestamp)`

  * Returns a value such that `set(key, value, timestamp_prev)` was called previously, with `timestamp_prev <= timestamp`.
  * If there are multiple such values, it returns the one with the largest `timestamp_prev`.
  * If there are no values, it returns the empty string (`""`).



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. All key/value strings are lowercase.
  2. All key/value strings have length in the range `[1, 100]`
  3. The `timestamps` for all `TimeMap.set` operations are strictly increasing.
  4. `1 <= timestamp <= 10^7`
  5. `TimeMap.set` and `TimeMap.get` functions will be called a total of `120000` times (combined) per test case.


**Tags:** Hash Table, Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/time-based-key-value-store