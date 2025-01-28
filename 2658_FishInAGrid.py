"""
2658. Maximum Number of Fish in a Grid
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        from typing import List

    # DFS helper function to explore the grid
        def dfs(r, c):
            # If the current cell is out of bounds or a land cell, return 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            # Store the number of fish in the current cell
            fish_count = grid[r][c]
            # Mark this cell as visited by setting its fish count to 0
            grid[r][c] = 0
            # Explore the four adjacent cells (up, down, left, right)
            fish_count += dfs(r + 1, c)
            fish_count += dfs(r - 1, c)
            fish_count += dfs(r, c + 1)
            fish_count += dfs(r, c - 1)
            
            return fish_count
        
        max_fish = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:  # Start DFS if we find a water cell with fish
                    max_fish = max(max_fish, dfs(i, j))
        
        return max_fish

# Example usage
solution = Solution()
grid1 = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
grid2 = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]

print(solution.findMaxFish(grid1))  # Output: 7
print(solution.findMaxFish(grid2))  # Output: 1
