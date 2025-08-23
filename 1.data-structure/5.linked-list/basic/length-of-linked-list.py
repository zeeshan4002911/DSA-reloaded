"""
Given head of a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

Examples :

Input: head : 1->2->3->4->5

Output: 5
Explanation: Length of the linked list is 5, as there
are 5 nodes present in it.

Input: head : 2->4->6->7->5->1->0

Output: 7
Explanation: Length of the linked list is 7, as there
are 7 nodes present in it.

Constraints:
1 <= number of nodes <= 4*104
1 <= node->data <= 10^3

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self, head):
        count = 0
        curr = head

        while curr is not None:
            count += 1
            curr = curr.next

        return count


class main:
    arr = input("Enter the linked list: ").strip().split()
    size = len(arr)

    ll = LinkedList()
    prev_node = None
    if size >= 1:
        node = Node(arr[0])
        ll.head = node
        prev_node = node

    for i in range(1, size):
        node = Node(arr[i])
        if prev_node:
            prev_node.next = node
        prev_node = node

    print(ll.get_length(ll.head))


if __name__ == "__main__":
    main()
