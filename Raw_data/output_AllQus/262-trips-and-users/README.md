# [Trips and Users][title]

## Description

The `Trips` table holds all taxi trips. Each trip has a unique Id, while
Client_Id and Driver_Id are both foreign keys to the Users_Id at the `Users`
table. Status is an ENUM type of ('completed', 'cancelled_by_driver',
'cancelled_by_client').
        

The `Users` table holds all users. Each user has an unique Users_Id, and Role
is an ENUM type of ('client', 'driver', 'partner').
        

Write a SQL query to find the cancellation rate of requests made by unbanned
users between **Oct 1, 2013** and **Oct 3, 2013**. For the above tables, your
SQL query should return the following rows with the cancellation rate being
rounded to _two_ decimal places.
        

**Credits:**  
Special thanks to
[@cak1erlizhou](https://leetcode.com/discuss/user/cak1erlizhou) for
contributing this question, writing the problem description and adding part of
the test cases.


**Tags:** 

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/trips-and-users