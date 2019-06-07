# [Min Cost Climbing Stairs][title]

## Description

On a staircase, the `i`-th step has some non-negative cost `cost[i]` assigned
(0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find
minimum cost to reach the top of the floor, and you can either start from the
step with index 0, or the step with index 1.

**Example 1:**  
        

**Example 2:**  
        

**Note:**  

  1. `cost` will have a length in the range `[2, 1000]`.
  2. Every `cost[i]` will be an integer in the range `[0, 999]`.


**Tags:** Array, Dynamic Programming

**Difficulty:** Easy

## 思路

``` cpp

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if(cost.empty())
            return 0;
        int n = cost.size();
        vector<int> dp(n,0);
        dp[0] = cost[0];
        dp[1] = cost[1];
        for(int i=2; i<n; i++) {
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]);
        }
        return min(dp[n-1], dp[n-2]);
    }
};
```

[title]: https://leetcode.com/problems/min-cost-climbing-stairs