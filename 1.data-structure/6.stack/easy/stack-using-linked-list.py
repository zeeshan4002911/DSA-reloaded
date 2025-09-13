"""
Implement a stack using linked list. The stack should support the following operations:

    push(x): Insert element x onto the top of the stack.
    pop(): Remove the element from the top of the stack. If the stack is empty, do nothing.
    top(): Return the element at the top of the stack. If the stack is empty, return -1.
    size(): Return the number of elements in the stack.
"""


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, val):
        node = Node(val)
        # Connect node to beginning of linked list
        node.next = self._top
        # Assigning the head to new node
        self._top = node

        self._size += 1
        return f"{val} pushed successfully"

    def pop(self):
        if self._top is None:
            return "Underflow Error"

        # Cache value before removing the node
        data = self._top.data
        # Cache next node for traversing forward in linked list
        next_node = self._top.next
        # Detaching the next linked to break the link of head node
        self._top.next = None
        # Assigning the head to next node
        self._top = next_node

        self._size -= 1
        return f"{data} popped successfully"

    def top(self):
        if self._top is None:
            return "Underflow Error: Stack is empty"
        return f"Stack peek : {self._top.data}"

    def size(self):
        return self._size
    
    def is_empty(self):
        return self._top is None

    def print_stack(self):
        result = []
        curr = self._top
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    st = Stack()
    while True:
        print("push(a) / pop(r) / top(t) / size(s) / isEmpty(e) / display(d) / exit(q)")

        user_input = input().strip().split()[:2]
        if user_input[0] == "a":
            print(st.push(user_input[1]))
        elif user_input[0] == "r":
            print(st.pop())
        elif user_input[0] == "t":
            print(st.top())
        elif user_input[0] == "s":
            print(st.size())
        elif user_input[0] == "e":
            print(st.is_empty())
        elif user_input[0] == "d":
            print(st.print_stack())
        elif user_input[0] == "q":
            break


if __name__ == "__main__":
    main()
