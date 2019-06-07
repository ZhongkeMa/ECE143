# [All Nodes Distance K in Binary Tree][title]

## Description

We are given a binary tree (with root node `root`), a `target` node, and an
integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the
`target` node.  The answer can be returned in any order.



**Example 1:**
        



**Note:**

  1. The given tree is non-empty.
  2. Each node in the tree has unique values `0 <= node.val <= 500`.
  3. The `target` node is a node in the tree.
  4. `0 <= K <= 1000`.


**Tags:** Tree, Depth-first Search, Breadth-first Search

**Difficulty:** Medium

## 思路

``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.parents={}
        self.results=[]
        self.parents[root]=(None,None)
        
        targetNode=self.findNode(root,target)
        direction=None
        while targetNode!=None:
            self.findKNodes(targetNode,K,direction)
            direction,targetNode=self.parents[targetNode]
            K=K-1
            
        return self.results
    
    def findKNodes(self,node,k,direction):
        if node:
            if k==0:
                self.results.append(node.val)
            else:
                if direction==None:
                    self.findKNodes(node.left,k-1,None)
                    self.findKNodes(node.right,k-1,None)
                else:
                    if direction==1:
                        self.findKNodes(node.left,k-1,None)
                    else:
                         self.findKNodes(node.right,k-1,None)
        
    def findNode(self,node,target):
        if node.val==target.val:
            return node
        
        foundNode=None
        
        if node.left!=None:
            self.parents[node.left]=(0,node)
            foundNode=self.findNode(node.left,target)
            
        if foundNode==None and node.right!=None:
            self.parents[node.right]=(1,node)
            foundNode=self.findNode(node.right,target)
            
        return foundNode
        
```

[title]: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree