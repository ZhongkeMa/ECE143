# [Prison Cells After N Days][title]

## Description

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the
following rules:

  * If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
  * Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the
row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: `cells[i] ==
1` if the `i`-th cell is occupied, else `cells[i] == 0`.

Given the initial state of the prison, return the state of the prison after
`N` days (and `N` such changes described above.)



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `cells.length == 8`
  2. `cells[i]` is in `{0, 1}`
  3. `1 <= N <= 10^9`


**Tags:** Hash Table

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/prison-cells-after-n-days