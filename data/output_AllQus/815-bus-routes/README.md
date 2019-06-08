# [Bus Routes][title]

## Description

We have a list of bus routes. Each `routes[i]` is a bus route that the i-th
bus repeats forever. For example if `routes[0] = [1, 5, 7]`, this means that
the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
forever.

We start at bus stop `S` (initially not on a bus), and we want to go to bus
stop `T`. Travelling by buses only, what is the least number of buses we must
take to reach our destination? Return -1 if it is not possible.
        

**Note:**

  * `1 <= routes.length <= 500`.
  * `1 <= routes[i].length <= 500`.
  * `0 <= routes[i][j] < 10 ^ 6`.


**Tags:** Breadth-first Search

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/bus-routes