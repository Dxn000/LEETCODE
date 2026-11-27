from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        # multiples_count[f] = number of items whose factor is divisible by f
        multiples_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            total = 0
            for mult in range(f, max_f + 1, f):
                total += freq[mult]
            multiples_count[f] = total

        # dp_unact[b]: max copies with budget b, current item not yet activated
        # dp_act[b]: max copies with budget b, current item activated
        dp_unact = [0] * (budget + 1)
        dp_act = [0] * (budget + 1)

        for f, price in items:
            if price > budget:
                continue

            bonus = multiples_count[f] - 1
            prev_unact = dp_unact[:]

            # Buy the 1st copy of current item -> activates item + grants free copies
            for b in range(price, budget + 1):
                candidate = prev_unact[b - price] + 1 + bonus
                if candidate > dp_act[b]:
                    dp_act[b] = candidate

            # Buy additional copies (2nd, 3rd, ...) of already-activated item
            for b in range(price, budget + 1):
                candidate = dp_act[b - price] + 1
                if candidate > dp_act[b]:
                    dp_act[b] = candidate

            # Carry best results forward into unactivated state for next item
            for b in range(budget + 1):
                if dp_act[b] > dp_unact[b]:
                    dp_unact[b] = dp_act[b]

        return max(dp_unact)