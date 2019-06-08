# [Champagne Tower][title]

## Description

We stack glasses in a pyramid, where the first row has 1 glass, the second row
has 2 glasses, and so on until the 100th row.  Each glass holds one cup
(250ml) of champagne.

Then, some champagne is poured in the first glass at the top.  When the top
most glass is full, any excess liquid poured will fall equally to the glass
immediately to the left and right of it.  When those glasses become full, any
excess champagne will fall equally to the left and right of those glasses, and
so on.  (A glass at the bottom row has it's excess champagne fall on the
floor.)

For example, after one cup of champagne is poured, the top most glass is full.
After two cups of champagne are poured, the two glasses on the second row are
half full.  After three cups of champagne are poured, those two cups become
full - there are 3 full glasses total now.  After four cups of champagne are
poured, the third row has the middle glass half full, and the two outside
glasses are a quarter full, as pictured below.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png)

Now after pouring some non-negative integer cups of champagne, return how full
the j-th glass in the i-th row is (both i and j are 0 indexed.)


        



**Note:**

  * `poured` will be in the range of `[0, 10 ^ 9]`.
  * `query_glass` and `query_row` will be in the range of `[0, 99]`.




**Tags:** 

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/champagne-tower