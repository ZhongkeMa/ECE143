# [New 21 Game][title]

## Description

Alice plays the following game, loosely based on the card game "21".

Alice starts with `0` points, and draws numbers while she has less than `K`
points.  During each draw, she gains an integer number of points randomly from
the range `[1, W]`, where `W` is an integer.  Each draw is independent and the
outcomes have equal probabilities.

Alice stops drawing numbers when she gets `K` or more points.  What is the
probability that she has `N` or less points?

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Note:**

  1. `0 <= K <= N <= 10000`
  2. `1 <= W <= 10000`
  3. Answers will be accepted as correct if they are within `10^-5` of the correct answer.
  4. The judging time limit has been reduced for this question.


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/new-21-game