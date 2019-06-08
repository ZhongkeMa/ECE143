# [Accounts Merge][title]

## Description

Given a list `accounts`, each element `accounts[i]` is a list of strings,
where the first element `accounts[i][0]` is a _name_ , and the rest of the
elements are _emails_ representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to
the same person if there is some email that is common to both accounts. Note
that even if two accounts have the same name, they may belong to different
people as people could have the same name. A person can have any number of
accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the
first element of each account is the name, and the rest of the elements are
emails **in sorted order**. The accounts themselves can be returned in any
order.

**Example 1:**  
        

**Note:**

* The length of `accounts` will be in the range `[1, 1000]`.
* The length of `accounts[i]` will be in the range `[1, 10]`.
* The length of `accounts[i][j]` will be in the range `[1, 30]`.


**Tags:** Depth-first Search, Union Find

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/accounts-merge