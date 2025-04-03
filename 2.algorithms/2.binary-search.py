class Search:
    def binary_search(self, arr, k):
        size = len(arr)
        low, high = 0, size - 1
        arr.sort()
        return self.binary_search_recursive(arr, k, low, high)

    def binary_search_recursive(self, arr, k, low, high):
        if low > high:
            return False
        mid = low + (high - low) // 2

        if k > arr[mid]:
            return self.binary_search_recursive(arr, k, mid + 1, high)
        elif k < arr[mid]:
            return self.binary_search_recursive(arr, k, low, mid - 1)
        else:
            return True

    def binary_search_iterative(self, arr, k, low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if k > arr[mid]:
                low = mid + 1
            elif k < arr[mid]:
                high = mid - 1
            else:
                return True
        return False


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter a value to search:", end=" ")
    k = int(input())
    src = Search()
    print(src.binary_search(arr, k))


if __name__ == "__main__":
    main()
