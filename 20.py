class Solution:

  def isValid(self, s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Pop the top element if stack is not empty, else assign a dummy value
        top_element = stack.pop() if stack else "#"

        # If the mapped opening bracket doesn't match the stack's top
        if mapping[char] != top_element:
          return False
      else:
        stack.append(char)

    return not stack