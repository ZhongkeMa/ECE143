# [Range Sum Query - Immutable][title]

## Description

Given an integer array _nums_ , find the sum of the elements between indices
_i_ and _j_ ( _i_ ≤ _j_ ), inclusive.

**Example:**  
            Given nums = [-2, 0, 3, -5, 2, -1]        sumRange(0, 2) -> 1    sumRange(2, 5) -> -1    sumRange(0, 5) -> -3    

**Note:**  

  1. You may assume that the array does not change.
  2. There are many calls to _sumRange_ function.


**Tags:** Dynamic Programming

**Difficulty:** Easy

## 思路

``` cpp
class NumArray {
private:
    vector<int> dp;
public:
    NumArray(vector<int> nums) {
        dp.push_back(0);
        for(int i=0; i<nums.size(); i++) {
            int temp = dp.back() + nums[i];
            dp.push_back(temp);
        }
    }
    
    int sumRange(int i, int j) {
        return dp[j+1] - dp[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
```

[title]: https://leetcode.com/problems/range-sum-query-immutable
