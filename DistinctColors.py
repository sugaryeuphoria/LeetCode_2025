"""
3160. Find the Number of Distinct Colors Among the Balls
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]

Explanation:



After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
Example 2:

Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

Output: [1,2,2,3,4]

Explanation:



After query 0, ball 0 has color 1.
After query 1, ball 0 has color 1, and ball 1 has color 2.
After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.

Constraints:

1 <= limit <= 109
1 <= n == queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 109
"""
import collections  # Import the collections module to use the Counter class

class Solution:
     # Define the method 'queryResults' that accepts limit and queries as input
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ans = []  # Initialize an empty list to store the results
        ballToColor = {}  # Initialize a dictionary to map each ball to its color
        colorCount = collections.Counter()
        # Iterate through each query in the list of queries
        for ball, color in queries:
            # Check if the ball already has a color assigned
            if ball in ballToColor:
                prevColor = ballToColor[ball]  # Get the previous color of the ball
                colorCount[prevColor] -= 1
                # If the count of the previous color becomes 0, remove it from the colorCount
                if colorCount[prevColor] == 0:
                    del colorCount[prevColor]
                     # Update the ball to the new color
            ballToColor[ball] = color
            # Increase the count of the new color
            colorCount[color] += 1
            # Append the number of distinct colors to the result list
            ans.append(len(colorCount))
            # Return the final result containing the number of distinct colors after each query
        return ans