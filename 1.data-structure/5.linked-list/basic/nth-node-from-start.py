"""
Given the head of a Singly Linked List and an index, The task is to find the node at the given index(1-based index) of the linked list. If no such index exists then return -1.

Examples :

Input: LinkedList: 1->2->3->4->5->6->7 , index = 3

Output: 3
Explanation: The Node value at index 3 is 3.

Input: LinkedList: 19->28->37->46->55 , index = 6

Output: -1
Explanation: As number of nodes are less than k so there is no node at index 6 , therefore our answer is -1.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= number of nodes <= 10^5
1 <= node->data , k <= 10^5
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def nth_node_from_start(self, head, index):
        curr = head

        length = 0
        while curr is not None:
            length += 1
            if length == index:
                return curr.data

            curr = curr.next

        return -1


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
    index = int(input("Enter the index form end (1-based): ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    print(solution.nth_node_from_start(head, index))


if __name__ == "__main__":
    main()
