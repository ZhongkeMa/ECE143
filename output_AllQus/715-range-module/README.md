# [Range Module][title]

## Description

A Range Module is a module that tracks ranges of numbers. Your task is to
design and implement the following interfaces in an efficient manner.

* `addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.

* `queryRange(int left, int right)` Returns true if and only if every real number in the interval `[left, right)` is currently being tracked.

* `removeRange(int left, int right)` Stops tracking every real number currently being tracked in the interval `[left, right)`.

**Example 1:**  
        

**Note:**

* A half open interval `[left, right)` denotes all real numbers `left <= x < right`.
* `0 < left < right < 10^9` in all calls to `addRange, queryRange, removeRange`.
* The total number of calls to `addRange` in a single test case is at most `1000`.
* The total number of calls to `queryRange` in a single test case is at most `5000`.
* The total number of calls to `removeRange` in a single test case is at most `1000`.


**Tags:** Segment Tree, Ordered Map

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/range-module