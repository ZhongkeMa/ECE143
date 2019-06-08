# [Frog Jump][title]

## Description

A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must
not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1
unit.

If the frog's last jump was _k_ units, then its next jump must be either _k_
\- 1, _k_ , or _k_ \+ 1 units. Note that the frog can only jump in the forward
direction.

**Note:**

  * The number of stones is ≥ 2 and is < 1,100.
  * Each stone's position will be a non-negative integer < 231.
  * The first stone's position is always 0.

**Example 1:**
        

**Example 2:**
        


**Tags:** Dynamic Programming

**Difficulty:** Hard

## 思路

``` python
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        steps={}
        for stone in stones:
            steps[stone]=set()
        
        steps[stones[0]].add(0)
        
        for stone in stones:
            stepPossibles=steps[stone]
            
            for stepPossible in stepPossibles:
                if stepPossible-1>0:
                    if stone+stepPossible-1 in steps:
                        if stone+stepPossible-1==stones[-1]:
                            return True
                        steps[stone+stepPossible-1].add(stepPossible-1)
                
                if stepPossible>0:
                    if stone+stepPossible in steps:
                        if stone+stepPossible==stones[-1]:
                            return True
                        steps[stone+stepPossible].add(stepPossible)

                if stone+stepPossible+1 in steps:
                    if stone+stepPossible+1==stones[-1]:
                        return True
                    steps[stone+stepPossible+1].add(stepPossible+1)
                
                
        return False
                    
            
                
            
        
```

[title]: https://leetcode.com/problems/frog-jump