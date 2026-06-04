class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append((r,c))

        length = 0
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                dir = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr,dc in dir:
                    R = r + dr
                    C = c + dc
                    if R in range(ROWS) and C in range(COLS) and grid[R][C] == 1:
                        grid[R][C] = 2
                        queue.append((R,C))
                        fresh -= 1
            length+=1 
        return length if fresh == 0 else -1
        