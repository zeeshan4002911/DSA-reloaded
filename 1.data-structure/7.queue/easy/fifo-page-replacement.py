"""
Common Page Replacement Techniques

    First In First Out (FIFO)
    Optimal Page replacement
    Least Recently Used (LRU)
    Most Recently Used (MRU)

1. First In First Out (FIFO)

This is the simplest page replacement algorithm. In this algorithm, the operating system keeps track of all pages in the memory in a queue, the oldest page is in the front of the queue. When a page needs to be replaced page in the front of the queue is selected for removal.

Example 1: Consider page reference string 1, 3, 0, 3, 5, 6, 3 with 3-page frames. Find the number of page faults using FIFO Page Replacement Algorithm.
FIFO - Page Replacement
FIFO - Page Replacement

    Initially, all slots are empty, so when 1, 3, 0 came they are allocated to the empty slots ---> 3 Page Faults.
    When 3 comes, it is already in memory so ---> 0 Page Faults.
    Then 5 comes, it is not available in memory, so it replaces the oldest page slot i.e 1. ---> 1 Page Fault.
    6 comes, it is also not available in memory, so it replaces the oldest page slot i.e 3 ---> 1 Page Fault.
    Finally, when 3 come it is not available, so it replaces 0 1-page fault.
"""

from queue import Queue


class Solution:
    def fifo_page_replacement(self, pages, capacity):
        page_fault = 0
        page_seen_set = set()
        page_queue = Queue()

        for page in pages:
            if len(page_seen_set) < capacity:
                # Adding into the queue while it's having space
                page_seen_set.add(page)
                page_queue.put(page)

                # Increasing the page fault
                page_fault += 1
            else:
                if page in page_seen_set:
                    # Skipping for the existing page in queue
                    continue
                else:
                    # Removing the oldest page from queue and seen set
                    oldest_page = page_queue.get()
                    page_seen_set.remove(oldest_page)

                    # Adding the new one in both queue and set
                    page_seen_set.add(page)
                    page_seen_set.add(page)

                    # Increasing the page fault
                    page_fault += 1

        return page_fault


def main():
    pages = input("Enter pages: ").strip().split()
    capacity = int(input("Enter capacity: ").strip())
    solution = Solution()
    print(solution.fifo_page_replacement(pages, capacity))


if __name__ == "__main__":
    main()
