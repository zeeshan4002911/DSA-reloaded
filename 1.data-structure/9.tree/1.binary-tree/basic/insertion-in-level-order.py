"""
Given a binary tree and a key, the task is to insert the key into the binary tree at the first position available in level order manner.
"""

import sys, os
from queue import Queue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree, BinaryTreeNode


class Solution:
    def insertion_in_level_order_ittr(self, root, key):
        if root is None:
            return []

        result = []
        queue = Queue()
        queue.put(root)
        is_inserted = False

        while not queue.empty():
            curr = queue.get()
            result.append(curr.data)

            # Insertion of key in the place of first empty node
            if curr.left is None and not is_inserted:
                new_node = BinaryTreeNode(key)
                curr.left = new_node
                is_inserted = True
            elif curr.right is None and not is_inserted:
                new_node = BinaryTreeNode(key)
                curr.right = new_node
                is_inserted = True
            
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)
        
        return result


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    key = input("Enter key: ").strip()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    result = soln.insertion_in_level_order_ittr(root, key)
    print(result)
    # bt.print_tree(root)



if __name__ == "__main__":
    main()
