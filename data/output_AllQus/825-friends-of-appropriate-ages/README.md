# [Friends Of Appropriate Ages][title]

## Description

Some people will make friend requests. The list of their ages is given and
`ages[i]` is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following
conditions are true:

  * `age[B] <= 0.5 * age[A] + 7`
  * `age[B] > age[A]`
  * `age[B] > 100 && age[A] < 100`

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people
will not friend request themselves.

How many total friend requests are made?

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



Notes:

  * `1 <= ages.length <= 20000`.
  * `1 <= ages[i] <= 120`.


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/friends-of-appropriate-ages