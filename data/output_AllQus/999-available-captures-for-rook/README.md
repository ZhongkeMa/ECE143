# [Available Captures for Rook][title]

## Description

On an 8 x 8 chessboard, there is one white rook.  There also may be empty
squares, white bishops, and black pawns.  These are given as characters 'R',
'.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal
directions (north, east, west, and south), then moves in that direction until
it chooses to stop, reaches the edge of the board, or captures an opposite
colored pawn by moving to the same square it occupies.  Also, rooks cannot
move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.



**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG)
        

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG)
        

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG)
        



**Note:**

  1. `board.length == board[i].length == 8`
  2. `board[i][j]` is either `'R'`, `'.'`, `'B'`, or `'p'`
  3. There is exactly one cell with `board[i][j] == 'R'`


**Tags:** Array

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/available-captures-for-rook