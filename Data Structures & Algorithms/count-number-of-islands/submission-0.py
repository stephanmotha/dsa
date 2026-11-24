class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y, seen):
            if x<0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in seen:
                return

            if grid[x][y] == "1":
                grid[x][y] = "0"
                seen.add((x, y))
                dfs(x-1, y, seen)
                dfs(x, y-1, seen)
                dfs(x+1, y, seen)
                dfs(x, y+1, seen)

            
        
        count = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, seen)

        return count





        