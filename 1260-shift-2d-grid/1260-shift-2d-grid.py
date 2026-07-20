class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
    
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                src_idx = (idx - k) % total
                result[i][j] = grid[src_idx // n][src_idx % n]
    
        return result