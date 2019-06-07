# [String to Integer (atoi)][title]

## Description

Implement `atoi` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this
character, takes an optional initial plus or minus sign followed by as many
numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the
integral number, which are ignored and have no effect on the behavior of this
function.

If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**

  * Only the space character `' '` is considered as whitespace character.
  * Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        


**Tags:** Math, String

**Difficulty:** Medium

## 思路

``` java
class Solution {
    public int myAtoi(String str) {
        String strTrim = str.trim();
        if(strTrim.length() == 0){
            return 0;
        }
        
        int sign = 1;
        int index = 0;
        long result = 0;
        if(strTrim.charAt(index) == '-' || strTrim.charAt(index) == '+'){
            sign = strTrim.charAt(index) == '-'?-1:1;
            index++;
        }
        
        while(index < strTrim.length()){
            int digit = strTrim.charAt(index) - '0';
            if(digit < 0 || digit > 9){
                break;
            }
            result = result*10 + digit;
            if(result > Integer.MAX_VALUE){
                if(sign == 1)
                    return Integer.MAX_VALUE;
                else
                    return Integer.MIN_VALUE;
            }
            index++;
        }
        
        return (int)(result*sign);
    }
}
```

[title]: https://leetcode.com/problems/string-to-integer-atoi