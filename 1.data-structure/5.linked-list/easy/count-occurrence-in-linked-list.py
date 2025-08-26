"""
Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.

Examples:

Input: Linked List: 1->2->1->2->1->3->1, key = 1

Output: 4
Explanation: 1 appears 4 times.

Input: Linked List: 1->2->1->2->1, key = 3

Output: 0
Explanation: 3 appears 0 times.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ number of nodes, key ≤ 10^5
1 ≤ data of node ≤ 10^5
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def count_occurence(self, head, key):
        if head is None:
            return

        curr = head
        count = 0
        while curr is not None:
            if curr.data == key:
                count += 1

            curr = curr.next

        return count


def main():
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
    key = int(input("Enter the key: ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)

    solution = Solution()
    print(solution.count_occurence(head, key))


if __name__ == "__main__":
    main()
