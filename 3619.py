from collections import deque

class Solution:
    # Keep the exact def line that LeetCode provides in your editor:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total_sum = grid[r][c]
                    grid[r][c] = 0  # mark visited
                    q = deque([(r, c)])

                    while q:
                        curr_r, curr_c = q.popleft()
                        for dr, dc in dirs:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                total_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                q.append((nr, nc))

                    if total_sum % k == 0:
                        ans += 1

        return ans