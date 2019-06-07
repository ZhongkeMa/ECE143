# [Climbing Stairs][title]

## Description

You are climbing a stair case. It takes _n_ steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

**Note:** Given _n_ will be a positive integer.

**Example 1:**
            Input: 2    Output: 2    Explanation: There are two ways to climb to the top.    1. 1 step + 1 step    2. 2 steps    

**Example 2:**
            Input: 3    Output: 3    Explanation: There are three ways to climb to the top.    1. 1 step + 1 step + 1 step    2. 1 step + 2 steps    3. 2 steps + 1 step    


**Tags:** Dynamic Programming

**Difficulty:** Easy

## 思路

``` cpp
class Solution {
public:
    int climbStairs(int n) {
        int first = 1;
        int second = 1;
        int third;
        if(n == 0 || n == 1)
            return 1;
        for(int i=2;i<=n;i++) {
            third = first + second;
            first = second;
            second = third;
        }
        return third;
    }
};
```

[title]: https://leetcode.com/problems/climbing-stairs
