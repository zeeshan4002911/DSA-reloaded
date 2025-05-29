"""
Given an array of integers arr[], sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.

Examples :

Input: arr[] = [5, 5, 4, 6, 4]
Output: [4, 4, 5, 5, 6]
Explanation: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since the frequencies are the same the smaller element comes first. So 4 4 comes first then comes 5 5. Finally comes 6. The output is 4 4 5 5 6.

Input: arr[] = [9, 9, 9, 2, 5]
Output: [9, 9, 9, 2, 5]
Explanation: The highest frequency here is 3. Element 9 has the highest frequency So 9 9 9 comes first. Now both 2 and 5 have the same frequency. So we print smaller elements first. The output is 9 9 9 2 5.

Constraints:
1 ≤ arr.size() ≤ 10^5
1 ≤ arr[i]≤ 10^5

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)
"""

from collections import Counter
import heapq


class Solution:
    def sort_by_frequency(self, arr):
        size = len(arr)
        arr.sort()
        # Matrix for storing frequency of element in [frequency, element] format
        mat: list[list[int, int]] = []

        # Count of frequency/occurence and insertion in matrix for recording
        count = 1
        for i in range(size - 1):
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                mat.append([count, arr[i]])
                count = 1
        mat.append([count, arr[size - 1]])

        # Sort in descending based on frequency
        mat.sort(key=lambda x: x[0], reverse=True)

        # write back elements based on frequency in original array
        k = 0
        for i in range(len(mat)):
            count = mat[i][0]
            while count:
                arr[k] = mat[i][1]
                k += 1
                count -= 1
        return arr

    # Using heap data strucute (max heap)
    def sort_by_frequency_heap(self, arr):
        freq = Counter(arr)
        # storing negative for max heap as heapq is by default min heap
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        result = []
        while heap:
            count, num = heapq.heappop(heap)
            result.extend([num] * -count)
        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.sort_by_frequency(arr))


if __name__ == "__main__":
    main()
