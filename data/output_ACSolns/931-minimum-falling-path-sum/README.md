# [Minimum Falling Path Sum][title]

## Description

Given a **square** array of integers `A`, we want the **minimum** sum of a
_falling path_ through `A`.

A falling path starts at any element in the first row, and chooses one element
from each row.  The next row's choice must be in a column that is different
from the previous row's column by at most one.



**Example 1:**
            Input: [[1,2,3],[4,5,6],[7,8,9]]    Output: 12    Explanation:    The possible falling paths are:    

  * `[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]`
  * `[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]`
  * `[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]`

The falling path with the smallest sum is `[1,4,7]`, so the answer is `12`.



**Note:**

  1. `1 <= A.length == A[0].length <= 100`
  2. `-100 <= A[i][j] <= 100`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

``` cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& A) {
        int rows = A.size();
        if(rows == 0)
            return 0;
        int cols = A[0].size();
        for(int i = rows - 2; i >= 0; i--) {
            for(int j = 0; j < cols; j++) {
                int base = A[i][j];
                A[i][j] += A[i+1][j];
                if(j-1>=0)
                    A[i][j] = min(A[i][j], base + A[i+1][j-1]);
                if(j+1<cols)
                    A[i][j] = min(A[i][j], base + A[i+1][j+1]);
            }
        }        
        int res = A[0][0];
        for(int i=1; i<cols; i++) {
            if(A[0][i] < res)
                res = A[0][i];
        }
        return res;
    }
    
};
```

[title]: https://leetcode.com/problems/minimum-falling-path-sum
