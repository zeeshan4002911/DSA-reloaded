class Sort:
    def bubble_sort(self, arr: list) -> None:
        """max of each pair to the end by swap"""
        size = len(arr)
        for i in range(size):
            swappedFlag = False
            for j in range(1, size - i):
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    swappedFlag = True

            if not swappedFlag:
                break


def main():
    arr = [int(value) for value in input().strip().split()]
    sort = Sort()
    sort.bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
