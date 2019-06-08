# [Video Stitching][title]

## Description

You are given a series of video clips from a sporting event that lasted `T`
seconds.  These video clips can be overlapping with each other and have varied
lengths.

Each video clip `clips[i]` is an interval: it starts at time `clips[i][0]` and
ends at time `clips[i][1]`.  We can cut these clips into segments freely: for
example, a clip `[0, 7]` can be cut into segments `[0, 1] + [1, 3] + [3, 7]`.

Return the minimum number of clips needed so that we can cut the clips into
segments that cover the entire sporting event (`[0, T]`).  If the task is
impossible, return `-1`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        



**Note:**

  1. `1 <= clips.length <= 100`
  2. `0 <= clips[i][0], clips[i][1] <= 100`
  3. `0 <= T <= 100`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/video-stitching