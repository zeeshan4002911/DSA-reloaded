"""
Given a linked list of n nodes and a key, the task is to check if the key is present in the linked list or not.

Example:

Input: n = 4, key = 3
1->2->3->4
Output: true
Explanation: 3 is present in Linked List, so the function returns true.

Constraint:
1 <= n <= 10^5
1 <= key <= 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def search_key(self, head, key):
        curr = head

        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next

        return False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class main:
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
    key = int(input("Enter the number to search: ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    print(solution.search_key(head, key))


if __name__ == "__main__":
    main()
