class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Step 1: Find all proper divisors for each possible length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Step 2: Precompute cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        # Helper to count changes to make grouped characters a palindrome
        def get_changes(sub):
            changes = 0
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    changes += 1
                left += 1
                right -= 1
            return changes

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_c = float('inf')
                sub_str = s[i:j+1]
                
                for d in divisors[length]:
                    current_d_cost = 0
                    # Check each of the d groups
                    for start in range(d):
                        group = sub_str[start::d]
                        current_d_cost += get_changes(group)
                    min_c = min(min_c, current_d_cost)
                
                cost[i][j] = min_c

        # Step 3: Dynamic Programming to partition into k parts
        # dp[i][p] = min changes to partition s[i:] into p parts
        memo = {}
        
        def dp(i, parts):
            if parts == 1:
                return cost[i][n - 1]
            if i >= n:
                return float('inf')
            if (i, parts) in memo:
                return memo[(i, parts)]
            
            res = float('inf')
            # Try all possible ending positions m for the current substring
            # Leave enough characters for the remaining (parts - 1) parts
            for m in range(i, n - parts + 1):
                res = min(res, cost[i][m] + dp(m + 1, parts - 1))
                
            memo[(i, parts)] = res
            return res

        return dp(0, k)
        