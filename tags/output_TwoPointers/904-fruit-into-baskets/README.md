# [Fruit Into Baskets][title]

## Description

In a row of trees, the `i`-th tree produces fruit with type `tree[i]`.

You **start at any tree  of your choice**, then repeatedly perform the
following steps:

  1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
  2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting
tree: you must perform step 1, then step 2, then back to step 1, then step 2,
and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you
want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        



**Note:**

  1. `1 <= tree.length <= 40000`
  2. `0 <= tree[i] < tree.length`


**Tags:** Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/fruit-into-baskets