from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1

        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] == 0:
                continue
            for mult in range(2 * f, n + 1, f):
                multiples_count[f] += freq[mult]

        min_price = min(price for _, price in items)

        priced_gains = []
        for factor, price in items:
            gain = multiples_count[factor] + (freq[factor] - 1)
            if gain > 0 and price < 2 * min_price:
                priced_gains.append((price, gain))

        priced_gains.sort(key=lambda x: x[0])

        total = 0
        for price, gain in priced_gains:
            if budget < price:
                break
            take = min(gain, budget // price)
            total += 2 * take
            budget -= take * price
            if take < gain:
                break

        total += budget // min_price
        return total