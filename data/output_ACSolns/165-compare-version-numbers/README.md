# [Compare Version Numbers][title]

## Description

Compare two version numbers _version1_ and _version2_.  
If `_version1_ > _version2_` return `1;` if `_version1_ < _version2_` return
`-1;`otherwise return `0`.

You may assume that the version strings are non-empty and contain only digits
and the `.` character.

The `.` character does not represent a decimal point and is used to separate
number sequences.

For instance, `2.5` is not "two and a half" or "half way to version three", it
is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number
to be `0`. For example, version number `3.4` has a revision number of `3` and
`4` for its first and second level revision number. Its third and fourth level
revision number are both `0`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        



**Note:**

  1. Version strings are composed of numeric strings separated by dots `.` and this numeric strings **may** have leading zeroes. 
  2. Version strings do not start or end with dots, and they will not be two consecutive dots.


**Tags:** String

**Difficulty:** Medium

## 思路

``` python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i,j=0,0
        while i<len(version1) or j<len(version2):
            a=0
            b=0
            
            while i<len(version1) and (version1[i]!='.'):
                a=10*a + int(version1[i])
                i+=1
                
            i+=1
                
            while j<len(version2) and (version2[j]!='.'):
                b=10*b + int(version2[j])
                j+=1
                
            j+=1
                
            if a>b:
                return 1
            elif a<b:
                return -1
            else:
                continue
            
        return 0
            
            
                
            
```

[title]: https://leetcode.com/problems/compare-version-numbers