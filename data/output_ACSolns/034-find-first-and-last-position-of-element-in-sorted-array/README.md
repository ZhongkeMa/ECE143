# [Find First and Last Position of Element in Sorted Array][title]

## Description

Given an array of integers `nums` sorted in ascending order, find the starting
and ending position of a given `target` value.

Your algorithm's runtime complexity must be in the order of _O_ (log _n_ ).

If the target is not found in the array, return `[-1, -1]`.

**Example 1:**
            Input: nums = [5,7,7,8,8,10], target = 8    Output: [3,4]

**Example 2:**
            Input: nums = [5,7,7,8,8,10], target = 6    Output: [-1,-1]


**Tags:** Array, Binary Search

**Difficulty:** Medium

## 思路

``` python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
                
    
        
```

[title]: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
