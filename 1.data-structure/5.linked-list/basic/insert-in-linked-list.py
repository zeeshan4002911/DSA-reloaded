"""
Given a singly linked list, a position pos, and data, the task is to insert that data into a linked list at the given position.

Examples:

    Input: 3->5->8->10, data = 2, pos = 2
    Output: 3->2->5->8->10

    Input: 3->5->8->10, data = 11, pos = 5
    Output: 3->5->8->10->11
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from linked_list_helper import LinkedList, Node


class Solution:
    def insert_at(self, head, pos, data):
        node = Node(data)

        # Insert at the beginning
        if pos == 1:
            node.next = head
            head = node
        else:
            # Insert in-between of linked list
            length = 0
            curr, prev = head, None
            while curr is not None:
                length += 1
                if length == pos:
                    prev.next = node
                    node.next = curr
                    break

                prev = curr
                curr = curr.next

            # Insert at the end of linked list
            if pos == length + 1:
                prev.next = node
            else:
                raise IndexError("Value of pos is out of range")
            
        return head


def main():
    arr = input("Enter the liked list: ").strip().split()
    pos = int(input("Enter the position for insertion: ").strip())
    data = input("Enter the value to be inserted: ").strip()

    ll = LinkedList()
    head = ll.append_all(arr)
    solution = Solution()
    head = solution.insert_at(head, pos, data)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
