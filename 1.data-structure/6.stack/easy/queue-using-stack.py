"""
Implement a Queue using two stack s1 and s2.

Examples:

Input:
enqueue(2)
enqueue(3)
dequeue()
enqueue(4)
dequeue()
Output: 2 3
Explanation:
enqueue(2) the queue will be [2]
enqueue(3) the queue will be [2, 3]
dequeue() the poped element will be 2
the queue will be [3]
enqueue(4) the queue will be [3, 4]
dequeue() the poped element will be [3].

Input:
enqueue(2)
dequeue()
dequeue()
Output: 2 -1

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Queue:
    queue = []

    def enqueue(self, X):
        self.queue.append(X)
        return

    def dequeue(self):
        st = []
        # Using another stack to tranfer all element except the last
        while len(self.queue) > 1:
            ele = self.queue.pop()
            st.append(ele)
        
        # Removal of queue first element
        if len(self.queue):
            result = self.queue.pop()
        else:
            return -1
        
        # Pushing back all the element to main queue
        while len(st) > 0:
            ele = st.pop()
            self.queue.append(ele)

        return result


def main():
    n = int(input("Enter the number of operation: ").strip())
    print(
        """Enter each operation and value in new line 
          with format - <enqueue/e> <num> or <dequeue/d>"""
    )
    solution = Queue()
    result = []
    while n != 0:
        line = input().strip().split()
        if line and len(line[0]):
            if line[0][0] == "e":
                solution.enqueue(line[1])
                n -= 1
                print(solution.queue)
            elif line[0][0] == "d":
                res = solution.dequeue()
                n -= 1
                result.append(res)
                print(solution.queue)
            else:
                print("Enter a valid format")
        else:
            print("Input can not be blank")

    print(result)


if __name__ == "__main__":
    main()
