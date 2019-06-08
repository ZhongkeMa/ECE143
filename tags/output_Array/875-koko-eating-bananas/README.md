# [Koko Eating Bananas][title]

## Description

Koko loves to eat bananas.  There are `N` piles of bananas, the `i`-th pile
has `piles[i]` bananas.  The guards have gone and will come back in `H` hours.

Koko can decide her bananas-per-hour eating speed of `K`.  Each hour, she
chooses some pile of bananas, and eats K bananas from that pile.  If the pile
has less than `K` bananas, she eats all of them instead, and won't eat any
more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas
before the guards come back.

Return the minimum integer `K` such that she can eat all the bananas within
`H` hours.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  * `1 <= piles.length <= 10^4`
  * `piles.length <= H <= 10^9`
  * `1 <= piles[i] <= 10^9`


**Tags:** Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/koko-eating-bananas