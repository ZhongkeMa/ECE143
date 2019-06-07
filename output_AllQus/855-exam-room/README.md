# [Exam Room][title]

## Description

In an exam room, there are `N` seats in a single row, numbered `0, 1, 2, ...,
N-1`.

When a student enters the room, they must sit in the seat that maximizes the
distance to the closest person.  If there are multiple such seats, they sit in
the seat with the lowest number.  (Also, if no one is in the room, then the
student sits at seat number 0.)

Return a class `ExamRoom(int N)` that exposes two functions: `ExamRoom.seat()`
returning an `int` representing what seat the student sat in, and
`ExamRoom.leave(int p)` representing that the student in seat number `p` now
leaves the room.  It is guaranteed that any calls to `ExamRoom.leave(p)` have
a student sitting in seat `p`.



**Example 1:**
        

​​​​​​​

**Note:**

  1. `1 <= N <= 10^9`
  2. `ExamRoom.seat()` and `ExamRoom.leave()` will be called at most `10^4` times across all test cases.
  3. Calls to `ExamRoom.leave(p)` are guaranteed to have a student currently sitting in seat number `p`.


**Tags:** Ordered Map

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/exam-room