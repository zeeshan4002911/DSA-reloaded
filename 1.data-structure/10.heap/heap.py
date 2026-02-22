"""
Custom Heap based on the heap structure following rules
1. It should be complete binary Tree
2. For current i-th node
    a. Parent of it i-th node = [(i - 1) / 2]
    b. Left child of i-th node = 2 * i + 1
    c. Right child of i-th node = 2 * i + 2
"""


class MaxHeap:
    def __init__(self):
        # Level order of the heap
        self._lst = []

    def print(self):
        print(self._lst)

    def insert(self, val):
        """
        Insert at the end of level order of heap and then Sift/Bubble up to right position
        """

        # Insertion at the end of the heap
        self._lst.append(val)
        i = len(self._lst) - 1

        while i > 0:
            parent_node = (i - 1) // 2

            if self._lst[parent_node] >= self._lst[i]:
                # Stopping the bubble up once the parent is greater
                break
            else:
                self._lst[parent_node], self._lst[i] = (
                    self._lst[i],
                    self._lst[parent_node],
                )
                i = parent_node

    def delete(self):
        """
        Swap with the last node and then Sift/Bubble down the root to right position
        """

        last = len(self._lst) - 1
        self._lst[last], self._lst[0] = self._lst[0], self._lst[last]
        pop_element = self._lst.pop()

        size = len(self._lst)
        i = 0
        while i < size:
            cache_curr_node = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < size and self._lst[i] < self._lst[left_child]:
                self._lst[i], self._lst[left_child] = (
                    self._lst[left_child],
                    self._lst[i],
                )
                i = left_child

            if right_child < size and self._lst[i] < self._lst[right_child]:
                self._lst[i], self._lst[right_child] = (
                    self._lst[right_child],
                    self._lst[i],
                )
                i = right_child

            if i == cache_curr_node:
                # Breaking once the current node (i) is in it's right position and there's no bubble down
                break

        return pop_element


def main():
    """
    Input format: 1 5 1 2 0 1, where 1 insert the next element to heap and 0 pop from heap
    """
    arr = input().strip().split()
    arr = list(map(int, arr))

    heap = MaxHeap()
    size = len(arr)
    i = 0
    while i < size:
        if arr[i] == 1:
            inp = arr[i + 1]
            heap.insert(inp)
            print("Inserted:", inp)
            heap.print()
            i += 1
        elif arr[i] == 0:
            res = heap.delete()
            print("Removed:", res)
            heap.print()
        i += 1


if __name__ == "__main__":
    main()
