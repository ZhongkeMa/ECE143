# [Exclusive Time of Functions][title]

## Description

On a single threaded CPU, we execute some functions.  Each function has a
unique id between `0` and `N-1`.

We store logs in timestamp order that describe when a function is entered or
exited.

Each log is a string with this format: `"{function_id}:{"start" |
"end"}:{timestamp}"`.  For example, `"0:start:3"` means the function with id
`0` started at the beginning of timestamp `3`.  `"1:end:2"` means the function
with id `1` ended at the end of timestamp `2`.

A function's _exclusive time_  is the number of units of time spent in this
function.  Note that this does not include any recursive calls to child
functions.

Return the exclusive time of each function, sorted by their function id.



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/04/05/diag1b.png)**
        



**Note:**

  1. `1 <= n <= 100`
  2. Two functions won't start or end at the same time.
  3. Functions will always log when they exit.




**Tags:** Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/exclusive-time-of-functions