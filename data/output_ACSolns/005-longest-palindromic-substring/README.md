# [Longest Palindromic Substring][title]

## Description

Given a string **s** , find the longest palindromic substring in **s**. You
may assume that the maximum length of **s** is 1000.

**Example 1:**
            Input:  "babad"    Output:  "bab"    **Note:**  "aba" is also a valid answer.    

**Example 2:**
            Input:  "cbbd"    Output:  "bb"    


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` java
class Solution {
    public String longestPalindrome(String s) {
        //Odd length palindrome
        //Even length palindrome
        if(s.length()==0){
            return "";
        }
        int maxlen = 1;
        int currLen = 0;
        int pos = 0;
        for(int i=1;i<s.length();i++){
                int low = i-1;
                int high = i;
                while(low>=0 && high<s.length() && s.charAt(low) == s.charAt(high)){
                    currLen = high-low+1;
                    if(currLen > maxlen){
                        maxlen = currLen;
                        pos = low;
                    }
                    low--;
                    high++;
                }
        }
        for(int i=1;i<s.length();i++){
                int low = i-1;
                int high = i+1;
                while(low>=0 && high<s.length() && s.charAt(low) == s.charAt(high)){
                    currLen = high-low+1;
                    if(currLen > maxlen){
                        maxlen = currLen;
                        pos = low;
                    }
                    low--;
                    high++;
                }
        }
        return s.substring(pos, pos+maxlen);
    }
}
```

[title]: https://leetcode.com/problems/longest-palindromic-substring
