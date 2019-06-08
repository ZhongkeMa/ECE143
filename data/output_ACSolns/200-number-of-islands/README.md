# [Number of Islands][title]

## Description

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid
are all surrounded by water.

**Example 1:**
            Input:    11110    11010    11000    00000        Output:  1    

**Example 2:**
            Input:    11000    11000    00100    00011        Output: 3    


**Tags:** Depth-first Search, Breadth-first Search, Union Find

**Difficulty:** Medium

## 思路

``` cpp
class Solution {
public:
    void dfs(vector<vector<char>> &grid, int r, int c) {
        int rows = grid.size();
        int cols = grid[0].size();
        grid[r][c] = '0';
        if(r+1<rows && grid[r+1][c] == '1')
            dfs(grid, r+1, c);
        if(r-1>=0 && grid[r-1][c] == '1')
            dfs(grid, r-1, c);
        if(c+1 < cols && grid[r][c+1] == '1')
            dfs(grid, r, c+1);
        if(c-1 >= 0 && grid[r][c-1] == '1')
            dfs(grid, r, c-1);
    }

    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        //vector<vector<bool>> visited (grid.size(), vector<bool> (grid[0].size(), false));
        for(int i=0; i<grid.size(); i++) {
            for(int j = 0; j < grid[0].size(); j++) {
                if(grid[i][j] == '1') {
                    res++;
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }
    
};
```

[title]: https://leetcode.com/problems/number-of-islands
