# [ZigZag Conversion][title]

## Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)
            P   A   H   N    A P L S I I G    Y   I   R    

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number
of rows:
            string convert(string s, int numRows);

**Example 1:**
            Input: s =  "PAYPALISHIRING", numRows = 3    Output:  "PAHNAPLSIIGYIR"    

**Example 2:**
            Input: s =  "PAYPALISHIRING", numRows = 4    Output:  "PINALSIGYAHRPI"    Explanation:        P     I    N    A   L S  I G    Y A   H R    P     I


**Tags:** String

**Difficulty:** Medium

## 思路

``` java
class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }
        List<StringBuilder> list = new ArrayList<>();
        for(int i=0;i<numRows;i++){
            list.add(new StringBuilder());
        }
        
        boolean goingDown = false;
        int curRow = 0;
        for(char c : s.toCharArray()){
            list.get(curRow).append(c);
            if(curRow == 0 || curRow ==numRows-1){
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1 : -1;
        }
        
        StringBuilder result = new StringBuilder();
        for(StringBuilder row: list){
            result.append(row);
        }
        return result.toString();
    }
}
```

[title]: https://leetcode.com/problems/zigzag-conversion
