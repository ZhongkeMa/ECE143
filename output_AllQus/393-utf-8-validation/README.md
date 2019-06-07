# [UTF-8 Validation][title]

## Description

A character in UTF8 can be from **1 to 4 bytes** long, subjected to the
following rules:

  1. For 1-byte character, the first bit is a 0, followed by its unicode code.
  2. For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:
               Char. number range  |        UTF-8 octet sequence

Given an array of integers representing the data, return whether it is a valid
utf-8 encoding.

**Note:**  
The input is an array of integers. Only the **least significant 8 bits** of
each integer is used to store the data. This means each integer represents
only 1 byte of data.

**Example 1:**
        

**Example 2:**
        


**Tags:** Bit Manipulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/utf-8-validation