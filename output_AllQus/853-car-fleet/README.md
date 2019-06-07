# [Car Fleet][title]

## Description

`N` cars are going to the same destination along a one lane road.  The
destination is `target` miles away.

Each car `i` has a constant speed `speed[i]` (in miles per hour), and initial
position `position[i]` miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and
drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the
same position.

A _car fleet_ is some non-empty set of cars driving  at the same position and
same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will
still be considered as one car fleet.

  
How many car fleets will arrive at the destination?



**Example 1:**
        

  
**Note:**

  1. `0 <= N <= 10 ^ 4`
  2. `0 < target <= 10 ^ 6`
  3. `0 < speed[i] <= 10 ^ 6`
  4. `0 <= position[i] < target`
  5. All initial positions are different.


**Tags:** Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/car-fleet