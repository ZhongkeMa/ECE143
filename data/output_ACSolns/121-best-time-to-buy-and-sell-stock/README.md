# [Best Time to Buy and Sell Stock][title]

## Description

Say you have an array for which the _i_ th element is the price of a given
stock on day _i_.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**
        

**Example 2:**
        


**Tags:** Array, Dynamic Programming

**Difficulty:** Easy

## 思路

``` cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty())
            return 0;
        int minPrice = prices[0];
        int max = 0;
        for(int i=1; i<prices.size(); i++) {
            minPrice = min(minPrice, prices[i]);
            if(prices[i] - minPrice > max)
                max = prices[i] - minPrice;
        }
        return max;
    }
};
```

[title]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock