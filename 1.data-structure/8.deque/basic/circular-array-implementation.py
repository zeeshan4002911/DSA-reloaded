"""
Operations on Deque:

    Mainly the following four basic operations are performed on queue:

        insertFront(): Adds an item at the front of Deque.
        insertRear(): Adds an item at the rear of Deque.
        deleteFront(): Deletes an item from front of Deque.
        deleteRear(): Deletes an item from rear of Deque.

    In addition to above operations, following operations are also supported

        frontEle(): Gets the front item from queue.
        RearEle(): Gets the last item from queue.
"""


class Deque:
    def __init__(self, capacity):
        self._capacity = capacity
        self._circular_arr = [None] * capacity
        self._size = 0
        self._front = 0

    def insert_front(self, val):
        if self._size == self._capacity:
            print("Deque is overflow")
            return

        self._front = (self._front + self._capacity - 1) % self._capacity
        self._circular_arr[self._front] = val
        self._size += 1
        return True

    def insert_rear(self, val):
        if self._size == self._capacity:
            print("Deque is overflow")
            return

        idx = ((self._front + self._size - 1) + 1) % self._capacity
        self._circular_arr[idx] = val
        self._size += 1
        return True

    def delete_front(self):
        if self._size == 0:
            print("Deque is underflow")
            return

        data = self._circular_arr[self._front]
        self._circular_arr[self._front] = None
        self._front = (self._front + 1) % self._capacity

        self._size -= 1
        return data

    def delete_back(self):
        if self._size == 0:
            print("Deque is underflow")
            return

        rear = (self._front + self._size - 1) % self._capacity
        data = self._circular_arr[rear]
        self._circular_arr[rear] = None

        self._size -= 1
        return data

    def get_front(self):
        if self._size == 0:
            print("Deque is empty")
            return
        return self._circular_arr[self._front]

    def get_back(self):
        if self._size == 0:
            print("Deque is empty")
            return
        return self._circular_arr[(self._front + self._size - 1) % self._capacity]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def erase(self):
        self._size = 0
        self._circular_arr = [] * self._capacity
        return True

    def pretty_print(self):
        if self._size == 0:
            print("Deque is empty")
            return

        start = self._front
        end = (self._front + self._size - 1) % self._capacity
        while start != end:
            print(self._circular_arr[start], end=" <-> ")
            start = (start + 1) % self._capacity
        print(self._circular_arr[start], end="")
        print()

    def get_list(self):
        arr = []
        for i in range(self._capacity):
            arr.append(self._circular_arr[i])
        return arr


def info():
    print(
        """
        pf <val> : push element at front of deque
        ppf : pop element from the front of deque
        pb <val> : push element at back of deque
        ppb : pop element from the back of deque
        gf : get front element of deque
        gb : get back elemenet of deque
        empty : Check whether the deque is empty or not
        clear : Clear or erase deque's all elements
        size : Get the size of deque
        pprint : Pretty print the deque
        list : Get the deque in list format
        q : exit
        """
    )


def main():
    capacity = int(input("Enter the capacity: ").strip())
    deque = Deque(capacity)
    print("Started!! Type info for available operations")

    while True:
        user_input = input().strip().split()[:2]
        if len(user_input) < 1:
            print("Enter a valid operation, type info for operation list")
            continue
        op = user_input[0]
        if op == "pf" and len(user_input) == 2:
            deque.insert_front(user_input[1])
        elif op == "pb" and len(user_input) == 2:
            deque.insert_rear(user_input[1])
        elif op == "ppf":
            print("Element Removed:", deque.delete_front())
        elif op == "ppb":
            print("Element Removed:", deque.delete_back())
        elif op == "gf":
            print("Front Element:", deque.get_front())
        elif op == "gb":
            print("Back Element:", deque.get_back())
        elif op == "empty":
            print(deque.is_empty())
        elif op == "clear":
            deque.erase()
        elif op == "size":
            print(deque.size())
        elif op == "pprint":
            deque.pretty_print()
        elif op == "list":
            print(deque.get_list())
        elif (op).lower() == "info":
            info()
        elif op == "q":
            break
        else:
            print("No valid operation provided, type info for valid operation list")


if __name__ == "__main__":
    main()
