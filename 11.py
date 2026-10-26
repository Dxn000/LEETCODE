class Solution:

  def maxArea(self, height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
      h_left = height[left]
      h_right = height[right]

      curr_area = (right - left) * min(h_left, h_right)
      if curr_area > max_water:
        max_water = curr_area

      # Advance pointer pointing to the shorter boundary
      if h_left < h_right:
        left += 1
      else:
        right -= 1

    return max_water