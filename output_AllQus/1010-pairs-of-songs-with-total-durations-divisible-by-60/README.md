# [Pairs of Songs With Total Durations Divisible by 60][title]

## Description

In a list of songs, the `i`-th song has a duration of `time[i]` seconds.

Return the number of pairs of songs for which their total duration in seconds
is divisible by `60`.  Formally, we want the number of indices `i < j` with
`(time[i] + time[j]) % 60 == 0`.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `1 <= time.length <= 60000`
  2. `1 <= time[i] <= 500`


**Tags:** Array

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60