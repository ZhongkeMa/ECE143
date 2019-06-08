# [Reconstruct Itinerary][title]

## Description

Given a list of airline tickets represented by pairs of departure and arrival
airports `[from, to]`, reconstruct the itinerary in order. All of the tickets
belong to a man who departs from `JFK`. Thus, the itinerary must begin with
`JFK`.

**Note:**

  1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
  2. All airports are represented by three capital letters (IATA code).
  3. You may assume all tickets form at least one valid itinerary.

**Example 1:**
            Input:[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]    Output:["JFK", "MUC", "LHR", "SFO", "SJC"]    

**Example 2:**
            Input:[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]    Output:["JFK","ATL","JFK","SFO","ATL","SFO"]    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].                 But it is larger in lexical order.    


**Tags:** Depth-first Search, Graph

**Difficulty:** Medium

## 思路

``` python
from collections import defaultdict
import heapq
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
            
        route = []
        
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            
        visit('JFK')
        return route[::-1]
    
            
            
        
```

[title]: https://leetcode.com/problems/reconstruct-itinerary
