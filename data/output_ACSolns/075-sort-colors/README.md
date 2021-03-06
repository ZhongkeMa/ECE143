# [Sort Colors][title]

## Description

Given an array with _n_ objects colored red, white or blue, sort them **[in-
place](https://en.wikipedia.org/wiki/In-place_algorithm) ** so that objects of
the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

**Note:**  You are not suppose to use the library's sort function for this
problem.

**Example:**
            Input: [2,0,2,1,1,0]    Output: [0,0,1,1,2,2]

**Follow up:**

  * A rather straight forward solution is a two-pass algorithm using counting sort.  
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
array with total number of 0's, then 1's and followed by 2's.

  * Could you come up with a one-pass algorithm using only constant space?


**Tags:** Array, Two Pointers, Sort

**Difficulty:** Medium

## 思路

``` python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        red, white, blue = 0, 0, len(nums)-1
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                
                
                
        
```

[title]: https://leetcode.com/problems/sort-colors
