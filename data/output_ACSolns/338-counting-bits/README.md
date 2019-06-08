# [Counting Bits][title]

## Description

Given a non negative integer number **num**. For every numbers **i** in the
range **0 ≤ i ≤ num** calculate the number of 1's in their binary
representation and return them as an array.

**Example 1:**
            Input: 2    Output: [0,1,1]

**Example 2:**
            Input: 5    Output:[0,1,1,2,1,2]    

**Follow up:**

  * It is very easy to come up with a solution with run time **O(n*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
  * Space complexity should be **O(n)**.
  * Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.


**Tags:** Dynamic Programming, Bit Manipulation

**Difficulty:** Medium

## 思路

``` cpp
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res;
        for(int i=0; i<=num;i++) {
            cout << "here";
            res.push_back(countOnes(i));
        }
        return res;
    }
    int countOnes(int n) {
        int res = 0;
        while(n) {
            n = n&(n-1);
            res++;
        }
        return res;
    }
};


/*
0 -    0
1 -    1 
2 -   10
3 -   11
4 -   100
5 -   101
6 -   110
7  -  111
8  - 1000
9  - 1001
10 - 1010
11 - 1011
12 - 1100
13 - 1101
14 - 1110
15 - 1111

*/

//0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4
```

[title]: https://leetcode.com/problems/counting-bits
