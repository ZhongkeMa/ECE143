# [Knight Probability in Chessboard][title]

## Description

On an `N`x`N` chessboard, a knight starts at the `r`-th row and `c`-th column
and attempts to make exactly `K` moves. The rows and columns are 0 indexed, so
the top-left square is `(0, 0)`, and the bottom-right square is `(N-1, N-1)`.

A chess knight has 8 possible moves it can make, as illustrated below. Each
move is two squares in a cardinal direction, then one square in an orthogonal
direction.



![](https://assets.leetcode.com/uploads/2018/10/12/knight.png)



Each time the knight is to move, it chooses one of eight possible moves
uniformly at random (even if the piece would go off the chessboard) and moves
there.

The knight continues moving until it has made exactly `K` moves or has moved
off the chessboard. Return the probability that the knight remains on the
board after it has stopped moving.



**Example:**
        



**Note:**

  * `N` will be between 1 and 25.
  * `K` will be between 0 and 100.
  * The knight always initially starts on the board.


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/knight-probability-in-chessboard