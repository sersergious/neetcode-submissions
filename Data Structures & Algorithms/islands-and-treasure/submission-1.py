class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))
        
        def add(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or (r, c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r, c))
            q.append((r, c))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                for dr, dc in directions:
                    add(r + dr, c + dc)
            
            dist += 1

                    

