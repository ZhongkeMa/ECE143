# [Super Palindromes][title]

## Description

Let's say a positive integer is a  _superpalindrome_  if it is a palindrome,
and it is also the square of a palindrome.

Now, given two positive integers `L` and `R` (represented as strings), return
the number of superpalindromes in the inclusive range `[L, R]`.



**Example 1:**
            Input: L = "4", R = "1000"    Output: 4    **Explanation** : 4, 9, 121, and 484 are superpalindromes.    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.



**Note:**

  1. `1 <= len(L) <= 18`
  2. `1 <= len(R) <= 18`
  3. `L` and `R` are strings representing integers in the range `[1, 10^18)`.
  4. `int(L) <= int(R)`




**Tags:** Math

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/super-palindromes
