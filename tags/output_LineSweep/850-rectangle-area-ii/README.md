# [Rectangle Area II][title]

## Description

We are given a list of (axis-aligned) `rectangles`.  Each `rectangle[i] = [x1,
y1, x2, y2] `, where (x1, y1) are the coordinates of the bottom-left corner,
and (x2, y2) are the coordinates of the top-right corner of the `i`th
rectangle.

Find the total area covered by all `rectangles` in the plane.  Since the
answer may be too large, **return it modulo 10^9 + 7**.

![](https://s3-lc-
upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png)

**Example 1:**
        

**Example 2:**
        

**Note:**

  * `1 <= rectangles.length <= 200`
  * ` rectanges[i].length = 4`
  * `0 <= rectangles[i][j] <= 10^9`
  * The total area covered by all rectangles will never exceed `2^63 - 1` and thus will fit in a 64-bit signed integer.


**Tags:** Segment Tree, Line Sweep

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/rectangle-area-ii