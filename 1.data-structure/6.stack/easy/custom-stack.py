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

    def getLastElement(self):
        if self.top is None:
            return

        return f"last element:: {self.top.data}"

    def removeLastElement(self):
        if self.top is None:
            return

        data = self.top.data
        self.top = self.top.prev
        self.top.next = None
        return f"{data} removed successfully"

    def addElement(self, ele):
        node = Node(ele)
        if self.top is None:
            node.min = ele
            self.top = node
        else:
            node.min = min(self.top.min, ele)
            node.prev = self.top
            self.top.next = node
            self.top = node

        return f"{ele} inserted successfully" 

    def getMin(self):
        if self.top is None:
            return

        return f"min element:: {self.top.min}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.min = None


def main():
    c_st = CustomStack()
    while True:
        print(
            "GetLastElement(l) / RemoveLastElement(r) / AddElement(a) / GetMin(g)"
        )
        user_input = input().strip().split()[:2]
        if user_input[0] == "l":
            print(c_st.getLastElement())
        elif user_input[0] == "r":
            print(c_st.removeLastElement())
        elif user_input[0] == "a":
            print(c_st.addElement(user_input[1]))
        elif user_input[0] == "g":
            print(c_st.getMin())
        elif user_input[0] == "e":
            break


if __name__ == "__main__":
    main()
