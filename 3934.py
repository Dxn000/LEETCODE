from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        base1, mod1 = 1000003, 10**9 + 7
        base2, mod2 = 1000033, 10**9 + 9

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base1) % mod1
            pow2[i] = (pow2[i - 1] * base2) % mod2

        def has_unique_of_len(k: int) -> bool:
            h1 = 0
            h2 = 0
            for i in range(k):
                val = nums[i]
                h1 = (h1 * base1 + val) % mod1
                h2 = (h2 * base2 + val) % mod2

            counts = Counter([(h1, h2)])
            p1 = pow1[k - 1]
            p2 = pow2[k - 1]

            for i in range(k, n):
                out_val = nums[i - k]
                in_val = nums[i]

                h1 = ((h1 - out_val * p1) % mod1 * base1 + in_val) % mod1
                h2 = ((h2 - out_val * p2) % mod2 * base2 + in_val) % mod2
                counts[(h1, h2)] += 1

            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_len(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans