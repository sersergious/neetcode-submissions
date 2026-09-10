class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        area = 0

        def dfs(r, c):
            nonlocal area
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or grid[r][c] == 0):
                return
            
            area += 1
            grid[r][c] = 0

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    maxArea = max(maxArea, area)
                    area = 0
        
        return maxArea

