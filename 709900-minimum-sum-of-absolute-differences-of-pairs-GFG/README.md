# [Minimum Sum of Absolute Differences of Pairs](https://www.geeksforgeeks.org/problems/minimum-sum-of-absolute-differences-of-pairs/1?utm_medium=courseteam_practice_desc&utm_campaign=problem_of_the_day&utm_source=youtube)
## Easy
You are given two arrays A&nbsp;and B&nbsp;of equal length N. Your task is to pair each element of array A&nbsp;to an element in array B, such that the sum&nbsp;of the&nbsp;absolute differences of all the pairs is minimum.

Example 1:

Input:
N = 4
A = {4,1,8,7}
B = {2,3,6,5}
Output:
6
Explanation:
If we take the pairings as (1,2), (4,3),
(7,5), and (8,6), the sum will be S =
|1 - 2| + |4 - 3| + |7 - 5| + |8 - 6| = 6.
It can be shown that this is the minimum sum we can get.


&nbsp;

Example 2:

Input:
N = 3
A = {4,1,2}
B = {2,4,1}
Output:
0
Explanation:
If we take the pairings as (4,4), (1,1), and
(2,2), the sum will be S = |4 - 4| + |1 - 1| +
|2 - 2| = 0. It can be shown that this is the
minimum sum we can get.

&nbsp;

Your Task:

You don't need to read input or print anything. Your task is to complete the function findMinSum()&nbsp;which takes the arrays&nbsp;A[], B[],&nbsp;and its size N&nbsp;as inputs and returns the minimum sum of the absolute differences of the pairs.

&nbsp;

Expected Time Complexity:&nbsp;O(N*log(N))
Expected Auxiliary Space:&nbsp;O(1)

&nbsp;

Constraints:
1 &lt;= N&nbsp;&lt;= 105
0 &lt;= A[i] &lt;= 109
0 &lt;= B[i] &lt;= 109
Sum of N over all test cases doesn't exceeds 106
