class Solution:

  def isPalindrome(self, x: int) -> bool:
    # Negative numbers and non-zero numbers ending in 0 are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
      return False

    reversed_half = 0
    while x > reversed_half:
      reversed_half = reversed_half * 10 + x % 10
      x //= 10

    # For even-length numbers: x == reversed_half
    # For odd-length numbers: x == reversed_half // 10 (discards middle digit)
    return x == reversed_half or x == reversed_half // 10