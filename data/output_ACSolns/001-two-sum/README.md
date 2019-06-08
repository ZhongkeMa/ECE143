# [Two Sum][title]

## Description

Given an array of integers, return **indices** of the two numbers such that
they add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you
may not use the _same_ element twice.

**Example:**
        




**Tags:** Array, Hash Table

**Difficulty:** Easy

## 思路

``` java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i=0;i<nums.length;i++){
            int complement = target - nums[i];
            if(map.containsKey(complement)){
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i],i);
        }
        return null;
    }
}
```

[title]: https://leetcode.com/problems/two-sum