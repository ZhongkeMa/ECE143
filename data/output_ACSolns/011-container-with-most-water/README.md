# [Container With Most Water][title]

## Description

Given _n_ non-negative integers _a 1_, _a 2_, ..., _a n _, where each
represents a point at coordinate ( _i_ , _a i_). _n_ vertical lines are drawn
such that the two endpoints of line _i_ is at ( _i_ , _a i_) and ( _i_ , 0).
Find two lines, which together with x-axis forms a container, such that the
container contains the most water.

**Note:  **You may not slant the container and _n_ is at least 2.



![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this
case, the max area of water (blue section) the container can contain is 49.



**Example:**
            Input: [1,8,6,2,5,4,8,3,7]    Output: 49


**Tags:** Array, Two Pointers

**Difficulty:** Medium

## 思路

``` java
class Solution {
    public int maxArea(int[] height) {
       int high = height.length - 1;
       int low = 0;
        int area = 0;
        while(low<high){
            area = Math.max(area, Math.min(height[low], height[high]) * (high - low));
            if(height[low] > height[high])
                high--;
            else
                low++;
            
        }
        return area;
    }
}
```

[title]: https://leetcode.com/problems/container-with-most-water
