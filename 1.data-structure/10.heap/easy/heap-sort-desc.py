"""
Given an array of elements, sort the array in decreasing order using min heap.

Examples:

    Input : arr[] = {5, 3, 10, 1}
    Output : arr[] = {10, 5, 3, 1}

    Input : arr[] = {1, 50, 100, 25}
    Output : arr[] = {100, 50, 25, 1}
"""


class Solution:
    def heap_sort_desc_inplace(self, arr):
        n = len(arr)
        # Converting parameter arr to max heap
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i, arr, n)

        for n1 in range(n - 1, -1, -1):
            # Swapping the root with the last element
            arr[0], arr[n1] = arr[n1], arr[0]

            # Bubbling down the root to place it at it's rigth position in heap
            self.sift_down(0, arr, n1)

        return arr

    # Same as heapify method of heap_helper.py
    def sift_down(self, i, arr, n):
        curr_node = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # Move current node in case the parent is greater than it's children to maintain min heap property
        if left_child < n and arr[curr_node] > arr[left_child]:
            curr_node = left_child
        if right_child < n and arr[curr_node] > arr[right_child]:
            curr_node = right_child

        if i != curr_node:
            # Swapping the parent with it's smaller value child
            arr[i], arr[curr_node] = arr[curr_node], arr[i]
            self.sift_down(curr_node, arr, n)


def main():
    arr = input("Enter array: ").strip().replace(",", " ").split()
    arr = [int(val) for val in arr]

    soln = Solution()
    soln.heap_sort_desc_inplace(arr)
    print(arr)


if __name__ == "__main__":
    main()
