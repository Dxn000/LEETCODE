class Solution:

  def myAtoi(self, s: str) -> int:
    i = 0
    n = len(s)

    # 1. Skip leading whitespace
    while i < n and s[i] == ' ':
      i += 1

    if i == n:
      return 0

    # 2. Determine sign
    sign = 1
    if s[i] == '-':
      sign = -1
      i += 1
    elif s[i] == '+':
      i += 1

    # 3. Read digits and assemble number
    result = 0
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    while i < n and s[i].isdigit():
      digit = ord(s[i]) - ord('0')

      # Check overflow before multiplying
      if result > (INT_MAX - digit) // 10:
        return INT_MAX if sign == 1 else INT_MIN

      result = result * 10 + digit
      i += 1

    return result * sign