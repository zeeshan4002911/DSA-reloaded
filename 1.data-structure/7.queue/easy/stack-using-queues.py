"""
Implement a Stack using two queues q1 and q2.

Examples:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) stack will be [2]
push(3) stack will be [2 3]
pop()   popped element will be 3 the stack will be [2]
push(4) the stack will be [2 4]
pop()   popped element will be 4

Input:
push(2)
pop()
pop()
push(3)
Output: 2 -1
Explanation:
push( 2 ) stack will be [ 2 ]
pop( ) popped element will be 2
pop( ) stack is empty so popped element will be -1
push( ) stack will be [ 3 ]

Constraints:
1 ≤ queries.size ≤ 100
1 ≤ stack.size ≤ 100
Expected Complexities
Time Complexity: O(n) for push() and O(1) for pop() (or vice-versa).
Auxiliary Space: O(1) for both push() and pop().
"""

from queue import Queue


class Stack:
    def __init__(self):
        # Main queue which should behave like stack
        self._queue = Queue()

    def push(self, val):
        # Push operation in O(1) time complexity
        self._queue.put(val)
        return True

    def pop(self):
        # For underflow stack return -1
        if self._queue.empty():
            return -1
        
        # Dequeue all the element and enqueue to another queue except the last tail
        _queue_helper = Queue()
        data = None
        while not self._queue.empty():
            ele = self._queue.get()
            if self._queue.empty():
                data = ele
            else:
                _queue_helper.put(ele)
        
        # Transfering all the element back to original queue
        while not _queue_helper.empty():
            self._queue.put(_queue_helper.get())
        
        return data

    def print_stack(self):
        arr = []
        for ele in self._queue.queue:
            arr.append(ele)
        return arr


def main():
    n = int(input("Enter the number of operation: ").strip())
    print(
        """Enter each operation and value in new line 
           with format - <push(1)> <num> OR <pop(0)>"""
    )
    st = Stack()
    result = []

    while n != 0:
        line = input().strip().split()
        if line and len(line[0]):
            if line[0][0] == "1":
                st.push(line[1])
                n -= 1
                print(st.print_stack())
            elif line[0][0] == "0":
                res = st.pop()
                n -= 1
                result.append(res)
                print(st.print_stack())
            else:
                print("Enter a valid format")
        else:
            print("Input can not be blank")

    print("Result:", result)


if __name__ == "__main__":
    main()
