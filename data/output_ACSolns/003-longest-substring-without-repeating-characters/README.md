# [Longest Substring Without Repeating Characters][title]

## Description

Given a string, find the length of the **longest substring** without repeating
characters.

**Example 1:**
            Input: "abcabcbb"    Output: 3     Explanation: The answer is "abc", with the length of 3.     

**Example 2:**
            Input: "bbbbb"    Output: 1    Explanation: The answer is "b", with the length of 1.    

**Example 3:**
            Input: "pwwkew"    Output: 3    Explanation: The answer is "wke", with the length of 3.                  Note that the answer must be a **substring** , "pwke" is a _subsequence_ and not a substring.    


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
