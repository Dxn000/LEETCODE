# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def removeNthFromEnd(
      self, head: ListNode | None, n: int
  ) -> ListNode | None:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast n + 1 steps ahead to maintain the gap
    for _ in range(n + 1):
      fast = fast.next

    # Move both until fast reaches the end
    while fast:
      fast = fast.next
      slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next