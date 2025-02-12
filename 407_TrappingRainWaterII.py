"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""
import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        #Check if the input grid is empty or has no rows
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        # Add all boundary cells to the heap (edges of the grid)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:  # Check if the cell is on the boundary
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))  # Push the boundary cell into the heap with its height and position
                    visited[i][j] = True

                    # Initialize a variable to store the total amount of trapped water
                    total_water = 0

                    # Directions for moving in the grid (right, down, left, up)
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    # Process the cells in the heap (start from the boundary cells)
                    while min_heap:
                        height, x, y = heapq.heappop(min_heap)
                        for dx, dy in directions:  # Loop through all 4 possible directions
                            nx, ny = x + dx, y + dy

                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                            visited[nx][ny] = True
                            total_water += max(0, height - heightMap[nx][ny])
                            heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return total_water