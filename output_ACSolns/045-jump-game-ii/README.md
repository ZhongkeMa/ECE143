# [Jump Game II][title]

## Description

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that
position.

Your goal is to reach the last index in the minimum number of jumps.

**Example:**
        

**Note:**

You can assume that you can always reach the last index.


**Tags:** Array, Greedy

**Difficulty:** Hard

## 思路

``` python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax=0
        nextMax=0
        steps=0
        
        if not nums or len(nums)==1:
            return 0
        
        n=len(nums)
        
        currMax=0
        nextMax=nums[0]
        steps=0
        
        for i in range(0,n-1):
            if i>currMax:
                steps+=1
                currMax=nextMax
                
            temp=i+nums[i]
            if temp>=n-1:
                return steps+1
            nextMax=max(temp,nextMax)
            
            if currMax>=n-1:
                return steps
            
        return steps
            
           
                
                
        return steps
            
        
```

[title]: https://leetcode.com/problems/jump-game-ii