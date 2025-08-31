"""
You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.

Examples:

Input: 1 -> 2 -> 3 -> 4
Output: 4 -> 3 -> 2 -> 1
Explanation: After reversing the linkedList


Input: 2 -> 7 -> 10 -> 9 -> 8
Output: 8 -> 9 -> 10 -> 7 -> 2
Explanation: After reversing the linked list


Input: 8
Output: 8
Explanation:

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def reverse_singly_linked_list(self, head):
        # For empty or single element head
        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        while curr is not None:
            # Cache curr -> next pointer for reference
            curr_next_ref = curr.next
            # Reversing the pointer direction
            curr.next = prev
            
            # Moving pointers to next node
            prev = curr
            curr = curr_next_ref
        
        return prev


def main():
    arr = input("Enter the linked list: ").strip().split()

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()

    head = solution.reverse_singly_linked_list(head)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
