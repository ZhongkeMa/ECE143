# [Stream of Characters][title]

## Description

Implement the `StreamChecker` class as follows:

  * `StreamChecker(words)`: Constructor, init the data structure with the given words.
  * `query(letter)`: returns true if and only if for some `k >= 1`, the last `k` characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.



**Example:**
        



**Note:**

  * `1 <= words.length <= 2000`
  * `1 <= words[i].length <= 2000`
  * Words will only consist of lowercase English letters.
  * Queries will only consist of lowercase English letters.
  * The number of queries is at most 40000.


**Tags:** Trie

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/stream-of-characters