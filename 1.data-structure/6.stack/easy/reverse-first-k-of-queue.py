"""
Given an integer k and a queue of integers, we need to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

    enqueue(x) : Add an item x to rear of queue
    dequeue() : Remove an item from front of queue
    size() : Returns number of elements in queue.
    front() : Finds front item.

Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.

"If the size of queue is smaller than the given k , then return the original queue."

Examples:

Input: q = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
Explanation: After reversing the first 3 elements from the given queue the resultant queue will be 3 2 1 4 5

Input: q = [4, 3, 2, 1], k = 4
Output: [1, 2, 3, 4]
Explanation: After reversing the first 4 elements from the given queue the resultant queue will be 1 2 3 4

Constraints:
1<=q[i]<=10^5
1<=q.size()<=10^5
1<=k<=10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

from collections import deque


class Solution:
    def reverse_first_k(self, q, k):
        size = len(q)
        
        # Special condition
        if size < k:
            return list(q)
        
        store_post_k = []
        st = []

        # Dequeue all the element after kth element
        for _ in range(k, size):
            store_post_k.append(q.pop())

        # Reverse due to stack behavior
        for _ in range(k):
            st.append(q.pop())
        
        # Appending the remaining unchanged part into the stack
        size = len(store_post_k)
        for i in range(size - 1, -1 , -1):
            st.append(store_post_k[i])

        return st


def main():
    queue = input("Enter the queue: ").strip().split()
    k = int(input("Enter the value of k: ").strip())
    solution = Solution()
    queue = deque(queue)
    print(solution.reverse_first_k(queue, k))


if __name__ == "__main__":
    main()
