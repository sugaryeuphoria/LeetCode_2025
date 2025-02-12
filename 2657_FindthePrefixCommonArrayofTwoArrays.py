"""
2657. Find the Prefix Common Array of Two Arrays
You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.
A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

Constraints:

1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
"""
# Importing List from the typing module for type hinting
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Initialize an empty list to store the prefix common counts
        prefix_common = []
        # Initialize sets to track numbers seen so far in A and B
        seen_in_a = set()
        seen_in_b = set()
        # Initialize a counter for the number of common elements
        common_count = 0
        # Iterate through the indices of the arrays
        for i in range(len(A)):
            # If the current element in A is already seen in B, increment the common count
            if A[i] in seen_in_b:
                common_count += 1
            # If the current element in B is already seen in A, increment the common count
            if B[i] in seen_in_a:
                common_count += 1
            # If the current elements in A and B are the same, increment the common count
            if A[i] == B[i]:
                common_count += 1
            # Add the current element of A to the seen_in_a set
            seen_in_a.add(A[i])
            # Add the current element of B to the seen_in_b set
            seen_in_b.add(B[i])
            # Append the current common count to the prefix_common list
            prefix_common.append(common_count)
            # Return the final list containing prefix common counts
        return prefix_common