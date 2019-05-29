# [Largest Number][title]

## Description

Given a list of non negative integers, arrange them such that they form the
largest number.

**Example 1:**
            Input: [10,2]    Output:  "210"

**Example 2:**
            Input: [3,30,34,5,9]    Output:  "9534330"    

**Note:** The result may be very large, so you need to return a string instead
of an integer.


**Tags:** Sort

**Difficulty:** Medium

## 思路

``` python
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def greater(a, b):
            if int(str(a)+str(b)) > int(str(b)+str(a)):
                return 1
            return -1

        nums=sorted(nums, cmp=greater,reverse=True)
        returnString=''.join(map(str,nums))
        
        i=0
        while i<len(returnString)-1:
            if returnString[i]=='0':
                i+=1
            else:
                break
                
        return returnString[i:]
        
        
```

[title]: https://leetcode.com/problems/largest-number
