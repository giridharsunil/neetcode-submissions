class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    maxarea = max(maxarea,self.dfs(grid, r, c, visit))
        return maxarea

    def dfs(self, grid, r, c, visit):
        if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visit or grid[r][c] == 0:
            return 0
        else:
            visit.add((r,c))
            return 1 + self.dfs(grid, r+1, c, visit) + self.dfs(grid, r-1, c, visit) + self.dfs(grid, r, c+1, visit) + self.dfs(grid, r, c-1, visit)
        