"""
Given a linked list, the task is to delete the linked list completely.

Examples:

    Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    Output: NULL
    Explanation: Linked List is Deleted.

    Input: head: 1 -> 12 -> 1 -> 4 -> 1 -> NULL
    Output: NULL
    Explanation: Linked List is Deleted.
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def clear_all(self, head):
        curr = head
        prev = None

        while curr is not None:
            if prev is not None:
                prev.data = None
                prev.next = None
            prev = curr
            curr = curr.next
        
        if prev is not None:
            prev.data = None
            prev.next = None
        
        if head is not None:
            head.data = None
            head.next = None
        
        return True


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    result = solution.clear_all(head)
    if result is True:
        head = None
    print("Delete status:", result)


if __name__ == "__main__":
    main()
