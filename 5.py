class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Loop terminated when s[left] != s[right] or boundaries exceeded
            # Valid palindrome slice is s[left + 1 : right]
            return left + 1, right - 1

        start = end = 0

        for i in range(len(s)):
            # Odd length palindrome
            l1, r1 = expand_around_center(i, i)
            # Even length palindrome
            l2, r2 = expand_around_center(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]