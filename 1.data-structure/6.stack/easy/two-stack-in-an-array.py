"""
Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.

twoStacks : Initialize the data structures and variables to be used to implement  2 stacks in one array.
push1 : pushes element into the first stack.
push2 : pushes element into the second stack.
pop1 : pops an element from the first stack and returns the popped element. If the first stack is empty, it should return -1.
pop2 : pops an element from the second stack and returns the popped element. If the second stack is empty, it should return -1.

Examples:

Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
Output: [3, 4, -1]
Explanation: push1(2) the stack1 will be [2]
push1(3) the stack1 will be [2,3]
push2(4) the stack2 will be [4]
pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence returned -1.

Input:
push1(1)
push2(2)
pop1()
push1(3)
pop1()
pop1()
Output: [1, 3, -1]
Explanation:
push1(1) the stack1 will be [1]
push2(2) the stack2 will be [2]
pop1()   the poped element will be 1 from stack1 and stack1 will be empty
push1(3) the stack1 will be [3]
pop1()   the poped element will be 3 from stack1 and stack1 will be empty
pop1()   the stack1 is now empty hence returned -1.

Input:
push1(2)
push1(3)
push1(4)
pop2()
pop2()
pop2()
Output: [-1, -1, -1]
Explanation:
push1(2) the stack1 will be [2]
push1(3) the stack1 will be [2,3]
push1(4) the stack1 will be [2,3,4]
pop2()   the stack2 is empty hence returned -1.
pop2()   the stack2 is empty hence returned -1.
pop2()   the stack2 is empty hence returned -1.

Constraints:
1 ≤ number of queries ≤ 10^4
1 ≤ number of elements in the stack ≤ 100
The sum of the count of elements in both the stacks < size of the given array

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class TwoStacks:
    def __init__(self):
        self.array = [None, None]
        self.st1_top_idx = -2
        self.st2_top_idx = -1

    # Function to push an integer into stack 1
    def push1(self, x):
        self.st1_top_idx += 2
        if self.st1_top_idx >= len(self.array):
            self.array.append(None)
            self.array.append(None)
        self.array[self.st1_top_idx] = x
        return

    # Function to push an integer into stack 2
    def push2(self, x):
        self.st2_top_idx += 2
        if self.st2_top_idx >= len(self.array):
            self.array.append(None)
            self.array.append(None)
        self.array[self.st2_top_idx] = x
        return

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.st1_top_idx < 0:
            return -1
        result = self.array[self.st1_top_idx]
        self.array[self.st1_top_idx] = None
        self.st1_top_idx -= 2
        self._shrink_array()
        return result

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.st2_top_idx < 0:
            return -1
        result = self.array[self.st2_top_idx]
        self.array[self.st2_top_idx] = None
        self.st2_top_idx -= 2
        self._shrink_array()
        return result

    def _shrink_array(self):
        used_space = max(self.st1_top_idx, self.st2_top_idx) + 2
        # Reducing the size of array to it's half to optimise space usage
        if used_space < len(self.array) // 2:
            new_size = len(self.array) // 2
            self.array = self.array[:new_size]


def main():
    n = int(input("Enter the number of operation: ").strip())
    print(
        """
        Enter stack (1/2) option (1 - push, no option for pop) and value in new line\n
        example: 1 1 10 for push of 10 on first stack\n
                 1 100 for pop from first stack, 100 is dummy
        """
    )
    tst = TwoStacks()
    result = []
    while n != 0:
        line = [int(val) for val in input().strip().split()]
        line_arr_length = len(line)
        if line_arr_length:
            if not (line[0] == 1 or line[0] == 2):
                print(
                    "Only two stack are supported", line[0], "should be either 1 or 2"
                )
                continue

            if line_arr_length == 3:
                # Push operation
                tst.push1(line[2]) if line[0] == 1 else tst.push2(line[2])
                n -= 1

            elif line_arr_length == 2:
                # Pop operation
                res = tst.pop1() if line[0] == 1 else tst.pop2()
                result.append(res)
                n -= 1

            else:
                print("Format is Invalid")
        else:
            print("Try Again")

    print(result)


if __name__ == "__main__":
    main()
