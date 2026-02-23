"""
A binary heap is a Binary Tree with the following properties:
1) Its a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it ).

Examples :

Input:
Q = 7
Queries:
insertKey(4)
insertKey(2)
extractMin()
insertKey(6)
deleteKey(0)
extractMin()
extractMin()
Output: [2, 6, -1]
Explanation: In the first test case for
query
insertKey(4) the heap will have  {4}
insertKey(2) the heap will be {2 4}
extractMin() removes min element from
             heap ie 2 and prints it
             now heap is {4}
insertKey(6) inserts 6 to heap now heap
             is {4 6}
deleteKey(0) delete element at position 0
             of the heap,now heap is {6}
extractMin() remove min element from heap
             ie 6 and prints it  now the
             heap is empty
extractMin() since the heap is empty thus
             no min element exist so -1
             is printed.

Input:
Q = 5
Queries:
insertKey(8)
insertKey(9)
deleteKey(1)
extractMin()
extractMin()
Output: [8, -1]

Constraints:
1 <= Q <= 10^4
1 <= x <= 10^4

Time Complexity: O(Q*log(size of Heap))
Auxiliary Space: O(1)
"""

"""
heap = [0 for i in range(101)]  # our heap to be used
"""

heap = [0 for i in range(101)]
# heap = []
curr_size = 0

"""
heap = [0 for i in range(101)]  # our heap to be used
"""


# Function to insert a value in Heap.
def insertKey(x):
    global curr_size
    global heap
    """
    Insert at the end of level order of heap and then Sift/Bubble up to right position
    """

    # Insertion at the end of the heap
    heap[curr_size] = x
    i = curr_size
    curr_size += 1

    while i > 0:
        parent_node = (i - 1) // 2

        if heap[parent_node] <= heap[i]:
            # Stopping the bubble up once the parent is greater
            break
        else:
            heap[parent_node], heap[i] = (
                heap[i],
                heap[parent_node],
            )
            i = parent_node


# Function to delete a key at ith index.
def deleteKey(i):
    global curr_size
    global heap
    if i >= curr_size:
        print("Index out of bound")
        return

    pop_element = heap[i]
    # Replacing the node to delete with +ve infinity
    heap[i] = float("inf")

    # Bubbling up +ve infinity to move it up to root
    while i > 0:
        parent_node = (i - 1) // 2

        if heap[parent_node] >= heap[i]:
            break
        else:
            heap[parent_node], heap[i] = (
                heap[i],
                heap[parent_node],
            )
            i = parent_node

    extractMin()
    return pop_element


# Function to extract minimum value in heap and then to store
# next minimum value at first index.
def extractMin():
    global curr_size
    global heap
    """
    Swap with the last node and then Sift/Bubble down the root to right position
    """
    if not heap:
        print("Heap is empty")
        print(-1)
        return -1

    last = curr_size - 1
    heap[last], heap[0] = heap[0], heap[last]
    pop_element = heap[curr_size - 1]
    heap[curr_size - 1] = -1
    curr_size -= 1

    size = curr_size
    i = 0
    while i < size:
        cache_curr_node = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and heap[i] > heap[left_child]:
            i = left_child

        if right_child < size and heap[i] > heap[right_child]:
            i = right_child

        if i == cache_curr_node:
            # Breaking once the current node (i) is in it's right position and there's no bubble down
            break
        else:
            heap[i], heap[cache_curr_node] = (
                heap[cache_curr_node],
                heap[i],
            )

    return pop_element


def main():
    arr = input("Enter the operation array: ").strip().split()
    size = len(arr)
    arr = list(map(int, arr))

    i = 0
    while i < size:
        if arr[i] == 1:
            inp = arr[i + 1]
            insertKey(inp)
            # print("insertKey:", inp, heap, curr_size)
            i += 1
        elif arr[i] == 2:
            deleteKey(arr[i + 1])
            # print("deleteKey:", arr[i + 1], heap, curr_size)
            i += 1
        elif arr[i] == 3:
            res = extractMin()
            # print("extractMin:", res, heap, curr_size)
        i += 1


if __name__ == "__main__":
    main()
