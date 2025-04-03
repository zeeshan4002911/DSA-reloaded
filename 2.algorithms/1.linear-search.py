class Search:
    def linear_search(self, arr, k):
        for ele in arr:
            if k == ele:
                return True
        return False


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter a value to search:", end=" ")
    k = int(input())
    src = Search()
    print(src.linear_search(arr, k))


if __name__ == "__main__":
    main()