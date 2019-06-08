# [Equal Rational Numbers][title]

## Description

Given two strings `S` and `T`, each of which represents a non-negative
rational number, return **True** if and only if they represent the same
number. The strings may use parentheses to denote the repeating part of the
rational number.

In general a rational number can be represented using up to three parts: an
_integer part_ , a  _non-repeating part,_ and a   _repeating part_. The number
will be represented  in one of the following three ways:

  * `<IntegerPart>` (e.g. 0, 12, 123)
  * `<IntegerPart><.><NonRepeatingPart>`  (e.g. 0.5, 1., 2.12, 2.0001)
  * `<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>` (e.g. 0.1(6), 0.9(9), 0.00(1212))

The repeating portion of a decimal expansion is conventionally denoted within
a pair of round brackets.  For example:

1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. Each part consists only of digits.
  2. The `<IntegerPart>` will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
  3. `1 <= <IntegerPart>.length <= 4 `
  4. `0 <= <NonRepeatingPart>.length <= 4 `
  5. `1 <= <RepeatingPart>.length <= 4`


**Tags:** Math

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/equal-rational-numbers