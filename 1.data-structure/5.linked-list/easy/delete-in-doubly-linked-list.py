"""
You are given a Doubly Linked List and an integer x. Remove the node at position x (positions are 1-indexed) from the list, and return the head of the updated list.

Examples:

Input: x = 3,

Output: 1 <-> 3
Explanation: After deleting the node at position 3 (position starts from 1), the updated linked list is 1 <-> 3.


Input: x = 1,

Output: 5 <-> 2 <-> 9
Explanation: After deleting the node at position 1, the updated linked list is 5 <-> 2 <-> 9.


Constraints:
1 ≤ x ≤ size of the linked list ≤ 10^6
0 ≤ node->data ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def append_all(self, lst):
        if lst is None:
            return None

        head = Node(lst[0])
        prev_node_ref = head

        size = len(lst)
        for i in range(1, size):
            node = Node(lst[i])

            # Forward connect of node (prev node -> next to point curr node)
            prev_node_ref.next = node
            # Backward connect of node (curr node -> prev to point to prev node)
            node.prev = prev_node_ref
            # Cache of curr node to prev node ref
            prev_node_ref = node

        self.head = head
        return head

    def pretty_print(self, head=None):
        curr = head or self.head
        while curr.next is not None:
            print(curr.data, "<-> ", end="")
            curr = curr.next
        print(curr.data)

    def remove_at(self, x, head=None):
        head = head or self.head
        if head is None:
            return None

        # Deletion of first postition
        if x == 1:
            head = head.next
            head.prev = None
        # Deletion of in-between element
        else:
            length = 0
            prev_node = None
            curr = head
            while curr.next is not None:
                length += 1
                if length == x:
                    prev_node.next = curr.next
                    curr.next.prev = prev_node
                    self.head = head
                    return head

                prev_node = curr
                curr = curr.next

            # Deletion of the end node
            if x == length + 1:
                prev_node.next = None
            else:
                raise IndexError("Value of x is greater than size of linked list")

        self.head = head
        return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def main():
    arr = input("Enter the linked list: ").strip().split()
    key = int(input("Enter pos for delete: ").strip())

    ll = LinkedList()
    head = ll.append_all(arr)
    head = ll.remove_at(key, head)
    ll.pretty_print(head)


if __name__ == "__main__":
    main()
