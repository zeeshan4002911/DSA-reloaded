"""
Given a singly linked list, your task is to remove every kth node from the linked list.

Examples:

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
Output: 1 -> 3 -> 5 -> 7

Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 -> 7.

Input: Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10

Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.

Expected Time Complexity:  O(n)
Expected Auxiliary Space:  O(1)

Constraints:
1 <= size of linked list <= 10^6
1 <= node->data <= 10^6
1 <= k <= size of linked list
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList, Node


class Solution:
    def remove_every_kth_node(self, head, k):
        if head is None:
            return

        curr = head
        prev = None
        length = 0

        # For k = 1, deletion of entire list will happen in this case it should return a node with -1 data
        if k == 1:
            head = Node(-1)
        else:
            while curr is not None:
                length += 1
                # Deletion on every kth node
                if length % k == 0:
                    prev.next = curr.next
                
                prev = curr
                curr = curr.next

        return head


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
    k = int(input("Enter the value of k: ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    head = solution.remove_every_kth_node(head, k)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
