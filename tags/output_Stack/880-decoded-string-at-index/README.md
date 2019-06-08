# [Decoded String at Index][title]

## Description

An encoded string `S` is given.  To find and write the _decoded_ string to a
tape, the encoded string is read **one character at a time**  and the
following steps are taken:

  * If the character read is a letter, that letter is written onto the tape.
  * If the character read is a digit (say `d`), the entire current tape is repeatedly written `d-1` more times in total.

Now for some encoded string `S`, and an index `K`, find and return the `K`-th
letter (1 indexed) in the decoded string.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `2 <= S.length <= 100`
  2. `S` will only contain lowercase letters and digits `2` through `9`.
  3. `S` starts with a letter.
  4. `1 <= K <= 10^9`
  5. The decoded string is guaranteed to have less than `2^63` letters.


**Tags:** Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/decoded-string-at-index