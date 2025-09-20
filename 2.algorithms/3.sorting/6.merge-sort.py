class Sort:
    def merge_sort(self, arr) -> None:
        size = len(arr)
        if size <= 1:
            return arr
        result = self.merge_sort_helper(arr, 0, size - 1)
        return result

    def merge_sort_helper(self, arr, low, high):
        if low >= high:
            return
        mid = low + (high - low) // 2
        self.merge_sort_helper(arr, low, mid)
        self.merge_sort_helper(arr, mid + 1, high)
        result = self.merge_helper(arr, low, mid, high)
        return result

    def merge_helper(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(len(temp)):
            arr[low + i] = temp[i]
        return arr


def main():
    arr = [int(value) for value in input().strip().split()]
    sort = Sort()
    result = sort.merge_sort(arr)
    print(result)


if __name__ == "__main__":
    main()
