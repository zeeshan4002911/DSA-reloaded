class Sort:
    def quick_sort(self, arr: list) -> None:
        """Partition based on pivot, keep till recursively single element"""
        size = len(arr)
        if size == 0:
            return
        self.quick_sort_helper(arr, 0, size - 1)

    def quick_sort_helper(self, arr, low, high):
        if low >= high:
            return
        pivot_index = self.partition_by_lomuto_algorithm(arr, low, high)
        self.quick_sort_helper(arr, low, pivot_index - 1)
        self.quick_sort_helper(arr, pivot_index + 1, high)
        # pivot_index = self.partition_by_hoare_algorithm(arr, low, high)
        # self.quick_sort_helper(arr, low, pivot_index)
        # self.quick_sort_helper(arr, pivot_index + 1, high)

    def partition_by_lomuto_algorithm(self, arr, low, high):
        """Pivot as end element and then single iteration for partitioning and placing the pivot in it's position"""
        pivot_index = high
        i = low
        for j in range(low, high):
            if arr[j] < arr[pivot_index]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        return i

    def partition_by_hoare_algorithm(self, arr, low, high):
        """Pivot can be anything, mostly start element, two-pointers for partitioning around pivot"""
        pivot_index = random.randrange(low, high)
        # Note: Need to use pivot instead of arr[pivot_index] inside while loops as due to swap pivot_index can have different value
        pivot = arr[pivot_index]
        i = low - 1
        j = high + 1
        while True:
            while True:
                i += 1
                if arr[i] >= pivot:
                    break
            while True:
                j -= 1
                if arr[j] <= pivot:
                    break
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]


def main():
    arr = [int(value) for value in input().strip().split()]
    sort = Sort()
    sort.quick_sort(arr)
    print(arr)


if __name__ == "__main__":
    import random
    main()
