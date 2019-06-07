# [Palindrome Number][title]

## Description

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Follow up:**

Coud you solve it without converting the integer to a string?


**Tags:** Math

**Difficulty:** Easy

## 思路

``` java
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0 || (x%10==0 && x!=0)){
            return false;
        }
        
        int rev = 0;
        while(x > rev){
            int num = x%10;
            x = x/10;
            rev = rev*10 + num;
        }
        
        return x == rev || x==rev/10;
    }
}
```

[title]: https://leetcode.com/problems/palindrome-number