###### What is the worst case time complexity of the following code :
```cpp
    /* 
    * V is sorted 
    * V.size() = N
    * The function is initially called as searchNumOccurrence(V, k, 0, N-1)
    */
    int searchNumOccurrence(vector<int> &V, int k, int start, int end) {
        if (start > end) return 0;
        int mid = (start + end) / 2;
        if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
        if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
        return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
    }

```
---
## *Solution*
### Time Complexity:

This code implements a recursive binary search to count the occurrences of a given number k in a sorted vector V of size N. Here's how the function works:  
Base Case: If start > end, the function returns 0 (no occurrences of k found).  
Recursive Steps:  
- Compute the midpoint mid = (start + end) / 2.
- If the middle element V[mid] is less than k, we recursively search the right half of the array (i.e., from mid + 1 to end).
- If the middle element V[mid] is greater than k, we recursively search the left half of the array (i.e., from start to mid - 1).
- If V[mid] == k, we count the occurrence of k at the middle position and then recursively search both the left and right halves of the array for additional occurrences.

Worst-Case Time Complexity Analysis:  
Recursive Depth:  
The function performs a binary search. Each recursive call reduces the problem size by half (similar to binary search), so the maximum depth of recursion is O(log⁡N)O(logN) because the search space is halved with each recursive call.

Work Done at Each Level:  
At each recursive step, the function makes:  
A constant amount of work to compute the midpoint mid.  
A constant time comparison (V[mid] < k, V[mid] > k, or V[mid] == k).  
This implies that at each level of recursion, the work done is O(1).

Total Recursive Calls:  
The function has to search both the left and right halves recursively when V[mid] == k, meaning for each occurrence of k at V[mid], it will continue searching both sides.  
In the worst case, if k appears at every position in the array, the function will need to recurse down both the left and right subarrays at each level.  
Thus, the recursion could potentially visit every element in the array in the worst case (for example, if k appears multiple times and you need to search both sides for each occurrence).

Therefore, in the worst case, the function will perform O(N) recursive calls, each of which takes constant time O(1) to perform the check and calculate the midpoint.

### Space COmplexity:

The function uses recursion. In each recursive call, the parameters start, end, and mid are passed, but no additional data structures are created (such as arrays or lists).  
The only auxiliary space used by the algorithm is for the function call stack due to recursion. This is the space used to store the recursive function calls until they are completed.  
Since the recursion depth is O(log⁡N), thus the space complexity is O(logN).

*Note: The space complexity is determined by the height of the recursive call stack.*