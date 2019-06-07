# [Median of Two Sorted Arrays][title]

## Description

There are two sorted arrays **nums1** and **nums2** of size m and n
respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume **nums1** and **nums2**  cannot be both empty.

**Example 1:**
        

**Example 2:**
        


**Tags:** Array, Binary Search, Divide and Conquer

**Difficulty:** Hard

## 思路

``` java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /*
            a[0] a[1].... a[i-1] | a[i].... a[m]
            b[0] b[1]..... b[j-1] | b[j] .... b[n]
        */
        
        int m = nums1.length;
        int n = nums2.length;
        
        if(m > n){
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        
        m = nums1.length;
        n = nums2.length;
        
        int iMin = 0, iMax = m, halflen = (m+n+1)/2;
        
        while(iMin <= iMax){
            int i = (iMin + iMax)/2;
            int j = halflen - i;
            
            if(i < iMax && nums2[j-1] > nums1[i]){
                iMin = i + 1;
            }
            else if(i > iMin && nums1[i-1] > nums2[j]){
                iMax = i - 1;
            }
            else{
                
                int maxLeft = 0;
                if( i == 0) 
                    maxLeft = nums2[j-1];
                else if(j == 0)
                    maxLeft = nums1[i-1];
                else
                    maxLeft = Math.max(nums1[i-1],nums2[j-1]);
                
                if((m+n) % 2 == 1) 
                    return maxLeft;
                
                int minRight = 0;
                if(i==m)
                    minRight = nums2[j];
                else if(j==n)
                    minRight = nums1[i];
                else
                    minRight = Math.min(nums1[i], nums2[j]);
                
                return (maxLeft + minRight)/2.0;
            }
            
        }
       return 0.0; 
    }
}
```

[title]: https://leetcode.com/problems/median-of-two-sorted-arrays