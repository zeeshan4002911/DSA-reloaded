"""
You are given the head of a singly linked list. Return an array containing the values of the nodes.

Examples:

Input:

Output: [1, 2, 3, 4, 5]
Explanation: The linked list contains 5 elements [1, 2, 3, 4, 5]. The elements are printed in a single line.

Input:

Output: [10, 20, 30, 40, 50, 60]
Explanation: The linked list contains 5 elements [10, 20, 30, 40, 50, 60]. The elements are printed in a single line.

Constraints :
1 ≤ numbers of nodes ≤ 10^5
1 ≤ node values ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def return_list(self, head):
        result = []
        curr = head

        while curr is not None:
            result.append(curr.data)
            curr = curr.next

        return result


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class main:
    arr = [int(value) for value in input("Enter the linked list: ").strip().split()]
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

    print(ll.return_list(ll.head))


if __name__ == "__main__":
    main()
