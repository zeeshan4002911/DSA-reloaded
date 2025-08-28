"""
Given the head, the head of a singly linked list, Returns true if the linked list is circular & false if it is not circular.

    A linked list is called circular if it is not NULL terminated and all nodes are connected in the form of a cycle.

Note: The linked list does not contain any inner loop.

Examples:

Input:
2->4->6->7->5->2->4......
Output: true
Explanation: As shown in figure the first and last node is connected, i.e. 5 --> 2

Input:
2->4->6->7->5->2->1
Output: false
Explanation: As shown in figure this is not a circular linked list.

Constraints:
1 <= number of nodes <= 100
1 <= node -> data <= 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def check_circular(self, head):
        if head is None:
            return

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # Floyd's Loop detection Algorithm - when slow pointer become same as fast
            if slow == fast:
                return True

        return False


def main():
    arr = input("Enter the linked list: ").strip().split()
    x = int(input("Enter the position of circular link: ").strip())

    ll = LinkedList()
    head = ll.append_all(arr, x)

    solution = Solution()
    print(solution.check_circular(head))


if __name__ == "__main__":
    main()
