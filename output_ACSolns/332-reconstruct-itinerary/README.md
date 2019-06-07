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
        

**Example 2:**
        


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