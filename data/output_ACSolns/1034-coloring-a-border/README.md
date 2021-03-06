# [Coloring A Border][title]

## Description

Given a 2-dimensional `grid` of integers, each value in the grid represents
the color of the grid square at that location.

Two squares belong to the same _connected component_ if and only if they have
the same color and are next to each other in any of the 4 directions.

The  _border_ of a connected component is  all the squares in the connected
component that are either 4-directionally adjacent to a square not in the
component, or on the boundary of the grid (the first or last row or column).

Given a square at location `(r0, c0)` in the grid and a `color`, color the
border of the connected component of that square with the given `color`, and
return the final `grid`.



**Example 1:**
            Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3    Output: [[3, 3], [3, 2]]    

**Example 2:**
            Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3    Output: [[1, 3, 3], [2, 3, 3]]    

**Example 3:**
            Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2    Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]



**Note:**

  1. `1 <= grid.length <= 50`
  2. `1 <= grid[0].length <= 50`
  3. `1 <= grid[i][j] <= 1000`
  4. `0 <= r0 < grid.length`
  5. `0 <= c0 < grid[0].length`
  6. `1 <= color <= 1000`


**Tags:** Depth-first Search

**Difficulty:** Medium

## 思路

``` cpp
class Solution {
public:
    void dfs(vector<vector<int>> &grid, int i, int j, int base) {
        grid[i][j] = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        if(i+1<rows && grid[i+1][j] == base)
            dfs(grid, i+1, j, base);
        if(j+1<cols && grid[i][j+1] == base)
            dfs(grid, i, j+1, base);
        if(i-1>=0 && grid[i-1][j] == base)
            dfs(grid, i-1, j, base);
        if(j-1>=0 && grid[i][j-1] == base)
            dfs(grid, i, j-1, base);
    }

    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0, int color) {
        vector<vector<int>> res = grid;
        int base = grid[r0][c0];
        dfs(grid, r0, c0, base);
        int rows = grid.size(); 
        int cols = grid[0].size();
        for(int i = 0; i<rows; i++) {
            for(int j = 0; j < cols; j++) {
                if(grid[i][j] == 0) {
                    if(i == 0 || j == 0 || i == rows - 1 || j == cols - 1)
                        res[i][j] = color;
                    if(i+1<rows && grid[i+1][j] != 0)
                        res[i][j] = color;
                    if(j+1<cols && grid[i][j+1] != 0)
                        res[i][j] = color;
                    if(i-1>= 0 && grid[i-1][j] != 0)
                        res[i][j] = color;
                    if(j-1>=0 && grid[i][j-1] != 0)
                        res[i][j] = color;
                }
            }
        }
        return res;
        
    }
    
};
```

[title]: https://leetcode.com/problems/coloring-a-border
