# [Shortest Completing Word][title]

## Description

Find the minimum length word from a given dictionary `words`, which has all
the letters from the string `licensePlate`. Such a word is said to _complete_
the given string `licensePlate`

Here, for letters we ignore case. For example, `"P"` on the `licensePlate`
still matches `"p"` on the word.

It is guaranteed an answer exists. If there are multiple answers, return the
one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For
example, given a `licensePlate` of `"PP"`, the word `"pair"` does not complete
the `licensePlate`, but the word `"supper"` does.

**Example 1:**  
        

**Example 2:**  
        

**Note:**  

  1. `licensePlate` will be a string with length in range `[1, 7]`.
  2. `licensePlate` will contain digits, spaces, or letters (uppercase or lowercase).
  3. `words` will have a length in the range `[10, 1000]`.
  4. Every `words[i]` will consist of lowercase letters, and have length in range `[1, 15]`.


**Tags:** Hash Table

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/shortest-completing-word