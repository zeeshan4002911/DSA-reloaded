"""
Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3. If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

Examples:

Input: Linked list: 1->2->3->4->5
Output: 3

Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.

Input: Linked list: 2->4->6->7->5->1
Output: 7

Explanation: The given linked list is 2->4->6->7->5->1 and its middle is 7.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= no. of nodes <= 10^5
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList, Node


class Solution:
    def middle_of_linked_list(self, head):
        if head is None:
            return

        curr = mid = head
        length = 0

        while curr is not None:
            length += 1
            # Increasing the mid pointer on every second step
            if length % 2 == 0:
                mid = mid.next

            curr = curr.next

        return mid.data


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    print(solution.middle_of_linked_list(head))


if __name__ == "__main__":
    main()
