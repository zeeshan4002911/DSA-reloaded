"""
You are given the head of a linked list and the number k, You have to return the kth node from the end of linkedList. If k is more than the number of nodes, then the return -1.

Examples

Input: LinkedList: 1->2->3->4->5->6->7->8->9, k = 2
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.

Input: LinkedList: 10->5->100->5, k = 5
Output: -1
Explanation: The given linked list is 10->5->100->5. Since 'k' is more than the number of nodes, the output is -1.

Constraints:
1 ≤ number of nodes ≤ 10^6
1 ≤ node->data , x ≤ 10^6
1 ≤ k ≤ 10^6


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def nth_node_from_end(self, head, index):
        forward_ptr = head
        backward_ptr = head

        length = 0
        # Two pointers - Difference between them remains given index from last
        # When forward pointer reaches the tail then backward will be in it's required position from end
        while forward_ptr is not None:
            if length >= index:
                backward_ptr = backward_ptr.next

            forward_ptr = forward_ptr.next
            length += 1

        if index > length:
            return -1
        return backward_ptr.data


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
    index = int(input("Enter the index form end (1-based): ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    print(solution.nth_node_from_end(head, index))


if __name__ == "__main__":
    main()
