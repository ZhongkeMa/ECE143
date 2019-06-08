# [Moving Stones Until Consecutive][title]

## Description

Three stones are on a number line at positions `a`, `b`, and `c`.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or
highest position stone), and move it to an unoccupied position between those
endpoints.  Formally, let's say the stones are currently at positions `x, y,
z` with `x < y < z`.  You pick up the stone at either position `x` or position
`z`, and move that stone to an integer position `k`, with `x < k < z` and `k
!= y`.

The game ends when you cannot make any more moves, ie. the stones are in
consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you
could have made?  Return the answer as an length 2 array: `answer =
[minimum_moves, maximum_moves]`



**Example 1:**
            Input: a = 1, b = 2, c = 5    Output: [1,2]    Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.    

**Example 2:**
            Input: a = 4, b = 3, c = 2    Output: [0,0]    Explanation: We cannot make any moves.    

**Example 3:**
            Input: a = 3, b = 5, c = 1    Output: [1,2]    Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.    



**Note:**

  1. `1 <= a <= 100`
  2. `1 <= b <= 100`
  3. `1 <= c <= 100`
  4. `a != b, b != c, c != a`






**Tags:** Brainteaser

**Difficulty:** Easy

## 思路

``` cpp
class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        vector<int> res;
        vector<int> holder = {a,b,c};
        sort(holder.begin(), holder.end());
        int maxer = holder[2];
        int miner = holder[0];
        int mider = holder[1];
        int max_steps = 0;
        int min_steps = 0; 
        if(mider - miner > 2 && maxer - mider > 2)
            min_steps = 2;
        
        else if((mider - miner == 2 && maxer - mider == 2) || (mider - miner == 1 && maxer - mider > 1) || (mider - miner > 1 && maxer - mider == 1) || (mider - miner == 2 && maxer - mider > 2) || (mider - miner > 2 && maxer - mider == 2))
            min_steps = 1;
        else if(mider - miner == 1 && maxer - mider == 1)
            min_steps = 0;
        while(miner + 1 != mider || mider + 1 != maxer) {
            if(miner + 1 < mider) {
                miner++;
                max_steps++;                
            }
            if(mider+1 < maxer) {
                maxer--;
                max_steps++;
            }
        }
        //cout << max_steps;
        res.push_back(min_steps);
        res.push_back(max_steps);
        return res;        
            

        
    }
};
```

[title]: https://leetcode.com/problems/moving-stones-until-consecutive
