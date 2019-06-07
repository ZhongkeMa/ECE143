# [Climbing Stairs][title]

## Description

You are climbing a stair case. It takes _n_ steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

**Note:** Given _n_ will be a positive integer.

**Example 1:**
        

**Example 2:**
        


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