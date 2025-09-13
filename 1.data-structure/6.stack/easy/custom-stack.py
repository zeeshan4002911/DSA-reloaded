"""
Create a customized data structure such that it has functions :-

    GetLastElement();
    RemoveLastElement();
    AddElement()
    GetMin()

All the functions should be of O(1)
"""


class CustomStack:
    def __init__(self):
        self.top = None

    def get_last_element(self):
        if self.top is None:
            return

        return f"last element:: {self.top.data}"

    def remove_Last_element(self):
        if self.top is None:
            return

        data = self.top.data
        next_node = self.top.next
        self.top.next = None
        self.top = next_node
        return f"{data} removed successfully"

    def add_element(self, ele):
        node = Node(ele)
        if self.top is None:
            node.min = ele
            self.top = node
        else:
            node.min = min(self.top.min, ele)
            node.next = self.top
            self.top = node

        return f"{ele} inserted successfully" 

    def get_min(self):
        if self.top is None:
            return

        return f"min element:: {self.top.min}"
    
    def print_stack(self):
        arr = []
        curr = self.top
        while curr is not None:
            data = (curr.data, curr.min)
            arr.append(data)
            curr = curr.next
        return arr


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = None


def main():
    c_st = CustomStack()
    while True:
        print(
            "GetLastElement(l) / RemoveLastElement(r) / AddElement(a) / GetMin(m) / display(d)"
        )
        user_input = input().strip().split()[:2]
        if user_input[0] == "l":
            print(c_st.get_last_element())
        elif user_input[0] == "r":
            print(c_st.remove_Last_element())
        elif user_input[0] == "a":
            print(c_st.add_element(int(user_input[1])))
        elif user_input[0] == "m":
            print(c_st.get_min())
        elif user_input[0] == "e":
            break
        elif user_input[0] == 'd':
            print(c_st.print_stack())


if __name__ == "__main__":
    main()
