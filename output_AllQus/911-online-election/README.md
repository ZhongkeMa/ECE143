# [Online Election][title]

## Description

In an election, the `i`-th vote was cast for `persons[i]` at time `times[i]`.

Now, we would like to implement the following query function:
`TopVotedCandidate.q(int t)` will return the number of the person that was
leading the election at time `t`.  

Votes cast at time `t` will count towards our query.  In the case of a tie,
the most recent vote (among tied candidates) wins.



**Example 1:**
        



**Note:**

  1. `1 <= persons.length = times.length <= 5000`
  2. `0 <= persons[i] <= persons.length`
  3. `times` is a strictly increasing array with all elements in `[0, 10^9]`.
  4. `TopVotedCandidate.q` is called at most `10000` times per test case.
  5. `TopVotedCandidate.q(int t)` is always called with `t >= times[0]`.


**Tags:** Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/online-election