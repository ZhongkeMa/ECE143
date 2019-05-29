# [Reverse Integer][title]

## Description

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**
            Input: 123    Output: 321    

**Example 2:**
            Input: -123    Output: -321    

**Example 3:**
            Input: 120    Output: 21    

**Note:**  
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [ −231,  231 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            sign=1
        else:
            sign=-1
            
        reversedNumber=self.reverseNumber(abs(x))
        
        if reversedNumber>(2**31-1):
            return 0
        else:
            return sign*reversedNumber
        
        
    def reverseNumber(self,x):
        num=x
        reversedNumber=0
        while num:
            reversedNumber=10*reversedNumber+num%10
            num=num//10
        
        return reversedNumber
```

[title]: https://leetcode.com/problems/reverse-integer
