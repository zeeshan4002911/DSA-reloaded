"""
You are given the head of a singly linked list and an integer x. Delete the xth node (1-based indexing) from the singly linked list.

Examples:

Input: x = 1,

Output: 2 -> 3 -> 1 -> 7
Explanation: After deleting the node at the 1st position (1-base indexing), the linked list is as


Input: x = 5,

Output: 2 -> 3 -> 4 -> 5
Explanation: After deleting the node at 5th position (1-based indexing), the linked list is as


Constraints:
1 ≤ size of linked list ≤ 10^5
1 ≤ x ≤ size of linked list

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def remove_at(self, head, pos):
        curr = head

        if curr is None:
            return curr

        # For the first position (head removal)
        if pos == 1:
            head = head.next
            curr.next = None
        # For the rest of position
        else:
            count = 0
            prev = None
            while curr is not None:
                count += 1
                if count == pos:
                    prev.next = curr.next
                    curr.next = None
                    break

                prev = curr
                curr = curr.next

        return head


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
    pos = int(input("Enter the position to remove: ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    head = solution.remove_at(head, pos)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
