class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 3:
            return 0
        
        # Since we can always make the low score 0, we only minimize (max - min)
        # across the 3 ways of changing two boundary elements.
        return min(
            nums[n - 3] - nums[0],  # Change 2 largest elements
            nums[n - 1] - nums[2],  # Change 2 smallest elements
            nums[n - 2] - nums[1],  # Change 1 smallest and 1 largest element
        )