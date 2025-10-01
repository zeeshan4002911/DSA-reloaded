"""
Given a singly linked list: A0 →A1 →...→An-2 →An-1 , reorder it to A0 →An-1 →A1 →An-2 →A2 →An-3 →...
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: Try to solve without using any auxiliary space.

Examples:

Input: LinkedList: 1->2->3
Output: 1->3->2
Explanation: Here n=3, so the correct order is A0 → A2 → A1

Input: LinkedList: 1->7->3->4
Output: 1->4->7->3
Explanation: Here n=4, so the correct order is A0 → A3 → A1 → A2

Constraints:
1 <= no. of nodes <= 10^6
0 <= node->data <= 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def reorder_linked_list(self, head):
        curr = head
        size = 0

        while curr.next is not None and curr.next.next is not None:
            size += 1
            # Skiping the node swap for even place (i.e., Reordered node)
            if size % 2 == 0:
                curr = curr.next
                continue

            cache_curr_next = curr.next
            last_node = curr
            last_prev_node = None
            # Traversing in linked list to find the last node
            while last_node.next is not None:
                last_prev_node = last_node
                last_node = last_node.next

            # Breaking the link of last node from linked list
            if last_prev_node is not None:
                last_prev_node.next = None

            # Reordering of the last node to be in even place
            curr.next = last_node
            last_node.next = cache_curr_next
            curr = curr.next

        return head


def main():
    arr = input("Enter the linked list values: ").strip().split()
    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    # In-place reorder
    solution.reorder_linked_list(head)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
