# [Longest Substring Without Repeating Characters][title]

## Description

Given a string, find the length of the **longest substring** without repeating
characters.

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        


**Tags:** Hash Table, Two Pointers, String, Sliding Window

**Difficulty:** Medium

## 思路

``` java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int j = 0;
        int maxlen = 0;
        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                j = Math.max(map.get(s.charAt(i)), j);
            }
            maxlen = Math.max(maxlen, i-j+1);
            map.put(s.charAt(i), i+1);
        }
        return maxlen;
    }
}
```

[title]: https://leetcode.com/problems/longest-substring-without-repeating-characters