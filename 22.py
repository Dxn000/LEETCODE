class Solution:

  def generateParenthesis(self, n: int) -> list[str]:
    result = []

    def backtrack(current_string, open_n, close_n):
      # Base case: if the string length is 2 * n, we have a valid combination
      if len(current_string) == 2 * n:
        result.append(current_string)
        return

      # Add an opening bracket if we haven't used all 'n' opening brackets
      if open_n < n:
        backtrack(current_string + "(", open_n + 1, close_n)

      # Add a closing bracket if there are unmatched opening brackets
      if close_n < open_n:
        backtrack(current_string + ")", open_n, close_n + 1)

    backtrack("", 0, 0)
    return result