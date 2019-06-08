# [My Calendar III][title]

## Description

Implement a `MyCalendarThree` class to store your events. A new event can
**always** be added.

Your class will have one method, `book(int start, int end)`. Formally, this
represents a booking on the half open interval `[start, end)`, the range of
real numbers `x` such that `start <= x < end`.

A _K-booking_ happens when **K** events have some non-empty intersection (ie.,
there is some time that is common to all K events.)

For each call to the method `MyCalendar.book`, return an integer `K`
representing the largest integer such that there exists a `K`-booking in the
calendar.

Your class will be called like this: `MyCalendarThree cal = new
MyCalendarThree();` `MyCalendarThree.book(start, end)`

**Example 1:**
        



**Note:**

  * The number of calls to `MyCalendarThree.book` per test case will be at most `400`.
  * In calls to `MyCalendarThree.book(start, end)`, `start` and `end` are integers in the range `[0, 10^9]`.




**Tags:** Segment Tree, Ordered Map

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/my-calendar-iii