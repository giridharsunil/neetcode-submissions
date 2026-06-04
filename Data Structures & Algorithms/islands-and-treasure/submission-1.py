class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == 2147483647:
                    grid[r][c] = length
                dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in dir:
                    R = r + dr
                    C = c + dc
                    if min(R, C) < 0 or R == ROWS or C == COLS or (R,C) in visit or grid[R][C]==-1:
                        continue
                    queue.append((R,C))
                    visit.add((R,C))
            length = length+1
