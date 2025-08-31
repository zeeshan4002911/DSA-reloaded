"""
 Given a singly linked list, the task is to convert it into a circular linked list.

Examples:

    Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
    Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 1 -> ....
    Explanation: Singly linked list is converted to circular by pointing last node to head.

    Input: head: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> NULL
    Output: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 2 -> ....
    Explanation: Singly linked list is converted to circular by pointing last node to head.
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def single_to_circular_conversion(self, head):
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        # Adding curr.next Null pointer to head to create circular linked list
        curr.next = head
        
        return head


def main():
    arr = input("Enter the linked list: ").strip().split()

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()

    head = solution.single_to_circular_conversion(head)
    ll.pretty_print(head, 1)


if __name__ == "__main__":
    main()
