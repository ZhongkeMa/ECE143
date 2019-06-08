# [Prefix and Suffix Search][title]

## Description

Given many `words`, `words[i]` has weight `i`.

Design a class `WordFilter` that supports one function, `WordFilter.f(String
prefix, String suffix)`. It will return the word with given `prefix` and
`suffix` with maximum weight. If no word exists, return -1.

**Examples:**
        



**Note:**

  1. `words` has length in range `[1, 15000]`.
  2. For each test case, up to `words.length` queries `WordFilter.f` may be made.
  3. `words[i]` has length in range `[1, 10]`.
  4. `prefix, suffix` have lengths in range `[0, 10]`.
  5. `words[i]` and `prefix, suffix` queries consist of lowercase letters only.




**Tags:** Trie

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/prefix-and-suffix-search