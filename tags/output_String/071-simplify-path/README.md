# [Simplify Path][title]

## Description

Given an **absolute path** for a file (Unix-style), simplify it. Or in other
words, convert it to the **canonical path**.

In a UNIX-style file system, a period `.` refers to the current directory.
Furthermore, a double period `..` moves the directory up a level. For more
information, see: [Absolute path vs relative path in
Linux/Unix](https://www.linuxnix.com/abslute-path-vs-relative-path-in-
linuxunix/)

Note that the returned canonical path must always begin with a slash `/`, and
there must be only a single slash `/` between two directory names. The last
directory name (if it exists) **must not**  end with a trailing `/`. Also, the
canonical path must be the **shortest** string  representing the absolute
path.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        

**Example 6:**
        


**Tags:** String, Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/simplify-path