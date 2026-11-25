""" """


class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        hash_set = set(nums)
        longest = 0

        for num in hash_set:
            # Beginning of sequence
            if (num - 1) not in hash_set:
                local_longest = 1
                while (num + local_longest) in hash_set:
                    local_longest += 1
                longest = max(local_longest, longest)
        
        return longest


def main():
    nums = input("Enter the nums: ").strip().replace(",", " ").split()
    nums = list(map(int, nums))
    print(Solution().longest_consecutive(nums))


if __name__ == "__main__":
    main()
