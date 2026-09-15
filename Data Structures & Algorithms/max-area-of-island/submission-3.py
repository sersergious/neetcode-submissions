class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or grid[r][c] != 1 or (r, c) in visited):
                return 0
            

            area = 1
            visited.add((r, c))
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
