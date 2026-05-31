class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == "1":
                    res+=1
                    self.dfs(grid,i,j,visit)
        return res
    def dfs(self, grid, r, c, visit):
        if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visit or grid[r][c] == "0":
            return 
        visit.add((r,c))
        self.dfs(grid, r+1, c, visit)
        self.dfs(grid, r-1, c, visit)
        self.dfs(grid, r, c+1, visit)
        self.dfs(grid, r, c-1, visit)
