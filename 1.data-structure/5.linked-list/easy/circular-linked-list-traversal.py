"""
Given a circular linked list, your task is to complete the method printList() that prints the linked list.

Input:
The printList function takes a single argument as input the reference pointer to the head of the linked list.
There are multiple test cases and for each test, the function will be called separately.
Output: You just need to print the LinkedList in the same line and the next line will be added by the Driver Code.

Example:

Input:
2
7
374 363 171 497 282 306 426
2
162 231
Output:
426 306 282 497 171 363 374
231 162

Note : Input items are inserted at the front of linked list that is why output is in reverse order.

Constraints:
1<=T<=50
1<=N<=50
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def circular_linked_list_traversal(self, head):
        if head is None:
            return

        slow = fast = head
        # Hare and Tortoise Algorithm
        while fast is not None and fast.next is not None:
            print(slow.data, end=" ")

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        return head


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]

    ll = LinkedList()
    # Circular linked list creation where tail is attach to first element
    head = ll.append_all(arr, 1)

    solution = Solution()
    head = solution.circular_linked_list_traversal(head)
    # ll.pretty_print(head)


if __name__ == "__main__":
    main()
