# [Find and Replace Pattern][title]

## Description

You have a list of `words` and a `pattern`, and you want to know which words
in `words` matches the pattern.

A word matches the pattern if there exists a permutation of letters `p` so
that after replacing every letter `x` in the pattern with `p(x)`, we get the
desired word.

( _Recall that a permutation of letters is a bijection from letters to
letters: every letter maps to another letter, and no two letters map to the
same letter._ )

Return a list of the words in `words` that match the given pattern.

You may return the answer in any order.



**Example 1:**
        



**Note:**

  * `1 <= words.length <= 50`
  * `1 <= pattern.length = words[i].length <= 20`


**Tags:** String

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/find-and-replace-pattern