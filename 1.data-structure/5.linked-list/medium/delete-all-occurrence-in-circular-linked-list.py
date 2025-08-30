"""
Given a Circular Linked List. The task is to delete the given node, key in the circular linked list, and reverse the circular linked list.

Note:

    You don't have to print anything, just return the head of the modified list in each function.
    Nodes may consist of Duplicate values.
    The key may or may not be present.

Examples:

Input: Linked List: 2->5->7->8->10, key = 8

Output: 10->7->5->2
Explanation: After deleting 8 from the given circular linked list, it has elements as 2, 5, 7, 10. Now, reversing this list will result in 10, 7, 5, 2 & the resultant list is also circular.

Input: Linked List: 1->7->8->10, key = 8

Output: 10->7->1
Explanation: After deleting 8 from the given circular linked list, it has elements as 1, 7,10. Now, reversing this list will result in 10, 7, 1 & the resultant list is also circular.

Input: Linked List: 3->6->4->10, key = 9
Output: 10->4->6->3
Explanation: As there no key present in the list, so simply reverse the list & the resultant list is also circular.

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
2 <= number of nodes, key  <= 10^5
1 <= node -> data <= 10^5
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList


class Solution:
    def deletion_all_occurrence_in_circular_linked_list(self, head, key):
        # Empty linked list check
        if head is None:
            return head

        # Deletion of the head node in case of size 1 circular linked list with match
        if head.next == head:
            return None if head.data == key else head

        prev = None
        curr = head
        while curr.next != head:
            if curr.data == key and prev is not None:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        # For the last node delete if it match
        if curr.data == key:
            prev.next = curr.next
        # If last node is not same as key then cache in prev
        else:
            prev = curr

        # Removal of head with last node ref if it match with key
        if head.data == key:
            prev.next = head.next
            head = head.next

        return head


def main():
    arr = input("Enter the linked list: ").strip().split()
    key = input("Enter key for delete: ").strip()

    ll = LinkedList()
    head = ll.append_all(arr, 1)

    solution = Solution()

    head = solution.deletion_all_occurrence_in_circular_linked_list(head, key)
    print("After Deletion")
    ll.pretty_print(head, 1)


if __name__ == "__main__":
    main()
