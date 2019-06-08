# [Walking Robot Simulation][title]

## Description

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot
can receive one of three possible types of commands:

  * `-2`: turn left 90 degrees
  * `-1`: turn right 90 degrees
  * `1 <= x <= 9`: move forward `x` units

Some of the grid squares are obstacles.

The `i`-th obstacle is at grid point `(obstacles[i][0], obstacles[i][1])`

If the robot would try to move onto them, the robot stays on the previous grid
square instead (but still continues following the rest of the route.)

Return the **square** of the maximum Euclidean distance that the robot will be
from the origin.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `0 <= commands.length <= 10000`
  2. `0 <= obstacles.length <= 10000`
  3. `-30000 <= obstacle[i][0] <= 30000`
  4. `-30000 <= obstacle[i][1] <= 30000`
  5. The answer is guaranteed to be less than `2 ^ 31`.


**Tags:** Greedy

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/walking-robot-simulation