"""
Implement a stack using doubly linked list. The stack should support the following operations:

    push(x): Insert element x onto the top of the stack.
    pop(): Remove the element from the top of the stack. If the stack is empty, do nothing.
    top(): Return the element at the top of the stack. If the stack is empty, return -1.
    size(): Return the number of elements in the stack.
"""


class CustomStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, val):
        node = Node(val)
        if self._top is None:
            self._top = node
        else:
            # Connect node to end of linked list
            self._top.next = node
            # Connect the new node prev to current head
            node.prev = self._top
            # Moving the head to next node
            self._top = self._top.next

        self._size += 1
        return f"{val} pushed successfully"

    def pop(self):
        if self._top is None:
            return "Underflow Error"

        # Cache value before removing the node
        data = self._top.data
        # Traversing back in linked list using prev pointer
        self._top = self._top.prev
        # Detaching the next linked to break the link of last node
        self._top.next = None

        self._size -= 1
        return f"{data} popped successfully"

    def top(self):
        if self._top is None:
            return "Underflow Error"
        return f"Stack peek : {self._top.data}"

    def size(self):
        return self._size

    def print_stack(self):
        result = []
        curr = self._top
        while curr is not None:
            result.append(curr.data)
            curr = curr.prev
        return result


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def main():
    c_st = CustomStack()
    while True:
        print("push(a) / pop(r) / top(t) / size(s) / display(d) / exit(e)")

        user_input = input().strip().split()[:2]
        if user_input[0] == "a":
            print(c_st.push(user_input[1]))
        elif user_input[0] == "r":
            print(c_st.pop())
        elif user_input[0] == "t":
            print(c_st.top())
        elif user_input[0] == "s":
            print(c_st.size())
        elif user_input[0] == "d":
            print(c_st.print_stack())
        elif user_input[0] == "e":
            break


if __name__ == "__main__":
    main()
