# [Camelcase Matching][title]

## Description

A query word matches a given `pattern` if we can insert **lowercase** letters
to the pattern word so that it equals the `query`. (We may insert each
character at any position, and may insert 0 characters.)

Given a list of `queries`, and a `pattern`, return an `answer` list of
booleans, where `answer[i]` is true if and only if `queries[i]` matches the
`pattern`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= queries.length <= 100`
  2. `1 <= queries[i].length <= 100`
  3. `1 <= pattern.length <= 100`
  4. All strings consists only of lower and upper case English letters.


**Tags:** String, Trie

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/camelcase-matching