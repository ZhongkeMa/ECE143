# [Longest Common Prefix][title]

## Description

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**
            Input: ["flower","flow","flight"]    Output:  "fl"    

**Example 2:**
            Input: ["dog","racecar","car"]    Output:  ""    Explanation: There is no common prefix among the input strings.    

**Note:**

All given inputs are in lowercase letters `a-z`.


**Tags:** String

**Difficulty:** Easy

## 思路

``` java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        int minLength = Integer.MAX_VALUE;
        if(strs == null || strs.length == 0)
            return "";
        for(String str: strs){
            minLength = Math.min(str.length(), minLength);
        }
        int low = 1;
        int high = minLength;
        while(low <= high){
            int mid = (low+high)/2;
            if(isCommonPrefix(strs, mid)){
                low = low + 1;
            } else{
                high = high - 1;
            }
        }
        return strs[0].substring(0,(low+high)/2);
    }
    
    boolean isCommonPrefix(String[] strs, int mid){
        String s = strs[0].substring(0, mid);
        for(int i=1;i<strs.length;i++){
            if(!strs[i].startsWith(s)){
                return false;
            }
        }
        return true;
    }
}
```

[title]: https://leetcode.com/problems/longest-common-prefix
