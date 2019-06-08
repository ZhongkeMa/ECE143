# [Most Profit Assigning Work][title]

## Description

We have jobs: `difficulty[i]` is the difficulty of the `i`th job, and
`profit[i]` is the profit of the `i`th job.

Now we have some workers. `worker[i]` is the ability of the `i`th worker,
which means that this worker can only complete a job with difficulty at most
`worker[i]`.

Every worker can be assigned at most one job, but one job can be completed
multiple times.

For example, if 3 people attempt the same job that pays $1, then the total
profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

**Example 1:**
        

**Notes:**

  * `1 <= difficulty.length = profit.length <= 10000`
  * `1 <= worker.length <= 10000`
  * `difficulty[i], profit[i], worker[i]`  are in range `[1, 10^5]`


**Tags:** Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/most-profit-assigning-work