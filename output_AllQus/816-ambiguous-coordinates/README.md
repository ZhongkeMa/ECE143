# [Ambiguous Coordinates][title]

## Description

We had some 2-dimensional coordinates, like `"(1, 3)"` or `"(2, 0.5)"`.  Then,
we removed all commas, decimal points, and spaces, and ended up with the
string `S`.  Return a list of strings representing all possibilities for what
our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started
with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
number that can be represented with less digits.  Also, a decimal point within
a number never occurs without at least one digit occuring before it, so we
never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all
coordinates in the final answer have exactly one space between them (occurring
after the comma.)
        



**Note:**

  * `4 <= S.length <= 12`.
  * `S[0]` = "(", `S[S.length - 1]` = ")", and the other elements in `S` are digits.




**Tags:** String

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/ambiguous-coordinates