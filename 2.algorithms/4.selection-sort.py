class Sort:
    def selection_sort(self, arr: list) -> None:
        """min to beginning by scanning unsorted portion"""
        size = len(arr)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]


def main():
    arr = [int(value) for value in input().strip().split()]
    sort = Sort()
    sort.selection_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
