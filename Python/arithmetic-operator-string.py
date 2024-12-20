'''
Python supports concatenating strings using the addition operator:

my_string = "Hello" + " " + "InterviewBit"
Python also supports multiplying strings to form a string with a repeating sequence:

my_string = "InterviewBit" * 5
Try the following example in the editor below.

Print “InterviewBit” 100 times without space on a same line.
'''

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    myStr = input()
    print(myStr * 100)
    return 0

if __name__ == '__main__':
    main()
