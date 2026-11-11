class Solution:

  def minimumCost(
      self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
  ) -> int:
    # 1. Find the overlapping units needed for both requirements
    common_need = min(need1, need2)

    # Cost for the overlapping part: compare buying Type 3 vs buying (Type 1 + Type 2)
    overlap_unit_cost = min(costBoth, cost1 + cost2)
    total_cost = common_need * overlap_unit_cost

    # 2. Handle remaining requirement for type 1 (if any)
    rem1 = need1 - common_need
    if rem1 > 0:
      unit_cost1 = min(cost1, costBoth)
      total_cost += rem1 * unit_cost1

    # 3. Handle remaining requirement for type 2 (if any)
    rem2 = need2 - common_need
    if rem2 > 0:
      unit_cost2 = min(cost2, costBoth)
      total_cost += rem2 * unit_cost2

    return total_cost