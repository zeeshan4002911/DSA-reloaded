"""
Given Circular linked list exchange the first and the last node.
The task should be done with only one extra node, you can not declare more than one extra node, and also you are not allowed to declare any other temporary variable.

Note: Extra node means the need of a node to traverse a list.

Examples:
    Input : 5 4 3 2 1
    Output : 1 4 3 2 5

    Input  : 6 1 2 3 4 5 6 7 8 9
    Output : 9 1 2 3 4 5 6 7 8 6
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def exchange_first_and_last_node(self, head):
        curr = head
        while curr.next != head:
            curr = curr.next

        # Swap of head and tail data of linked list
        curr.data, head.data = head.data, curr.data
        
        return head


def main():
    arr = input("Enter the linked list: ").strip().split()

    ll = LinkedList()
    head = ll.append_all(arr, 1)

    solution = Solution()

    head = solution.exchange_first_and_last_node(head)
    ll.pretty_print(head, 1)


if __name__ == "__main__":
    main()
