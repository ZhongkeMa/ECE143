# [Maximum Subarray][title]

## Description

Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

**Example:**
            Input: [-2,1,-3,4,-1,2,1,-5,4],    Output: 6    Explanation:  [4,-1,2,1] has the largest sum = 6.    

**Follow up:**

If you have figured out the O( _n_ ) solution, try coding another solution
using the divide and conquer approach, which is more subtle.


**Tags:** Array, Divide and Conquer, Dynamic Programming

**Difficulty:** Easy

## 思路

``` cpp
//Kadane Algo

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        //vector<int> dp(n,0);
        //dp[0] = nums[0];
        int sum = INT_MIN;
        int curr = 0;
        for(int i=0; i<nums.size(); i++) {
            //dp[i] = max(dp[i-1] + nums[i]
            curr = curr + nums[i];
            sum = max(sum, curr);
            if(curr < 0)
                curr = 0;
            //cout << i << " " << dp[i] << endl;
        }
        return sum;
    }
};
```

[title]: https://leetcode.com/problems/maximum-subarray
