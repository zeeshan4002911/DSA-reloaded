"""
You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

Examples:

Input: head = 3 <-> 4 <-> 5
Output: 5 <-> 4 <-> 3

Input: head = 75 <-> 122 <-> 59 <-> 196
Output: 196 <-> 59 <-> 122 <-> 75

Constraints:
1 ≤ number of nodes ≤ 10^6
0 ≤ node->data ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import DoublyLinkedList


class Solution:
    def reverse_doubly_linked_list(self, head):
        # For empty or single element linked list
        if head is None or head.next is None:
            return head

        curr = head
        prev = None
        while curr is not None:
            # Cache curr -> next pointer for reference
            curr_next_ref = curr.next
            # Swap of next and prev pointer for reverse
            curr.next, curr.prev = curr.prev, curr.next

            # Moving pointers to next node
            prev = curr
            curr = curr_next_ref

        return prev


def main():
    arr = input("Enter the linked list: ").strip().split()

    ll = DoublyLinkedList()
    head = ll.append_all(arr)

    solution = Solution()

    head = solution.reverse_doubly_linked_list(head)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
