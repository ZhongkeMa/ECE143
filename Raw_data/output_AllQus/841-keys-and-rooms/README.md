# [Keys and Rooms][title]

## Description

There are `N` rooms and you start in room `0`.  Each room has a distinct
number in `0, 1, 2, ..., N-1`, and each room may have some keys to access the
next room.

Formally, each room `i` has a list of keys `rooms[i]`, and each key
`rooms[i][j]` is an integer in `[0, 1, ..., N-1]` where `N = rooms.length`.  A
key `rooms[i][j] = v` opens the room with number `v`.

Initially, all the rooms start locked (except for room `0`).

You can walk back and forth between rooms freely.

Return `true` if and only if you can enter every room.

**Example 1:**
        

**Example 2:**
        

**Note:**

  1. `1 <= rooms.length <= 1000`
  2. `0 <= rooms[i].length <= 1000`
  3. The number of keys in all rooms combined is at most `3000`.


**Tags:** Depth-first Search, Graph

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/keys-and-rooms