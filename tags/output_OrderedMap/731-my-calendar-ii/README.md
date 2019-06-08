# [My Calendar II][title]

## Description

Implement a `MyCalendarTwo` class to store your events. A new event can be
added if adding the event will not cause a **triple** booking.

Your class will have one method, `book(int start, int end)`. Formally, this
represents a booking on the half open interval `[start, end)`, the range of
real numbers `x` such that `start <= x < end`.

A _triple booking_ happens when **three** events have some non-empty
intersection (ie., there is some time that is common to all 3 events.)

For each call to the method `MyCalendar.book`, return `true` if the event can
be added to the calendar successfully without causing a **triple** booking.
Otherwise, return `false` and do not add the event to the calendar.

Your class will be called like this: `MyCalendar cal = new MyCalendar();`
`MyCalendar.book(start, end)`

**Example 1:**
        



**Note:**

  * The number of calls to `MyCalendar.book` per test case will be at most `1000`.
  * In calls to `MyCalendar.book(start, end)`, `start` and `end` are integers in the range `[0, 10^9]`.




**Tags:** Ordered Map

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/my-calendar-ii