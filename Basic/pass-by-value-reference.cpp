/**
 * Geek is learning about functions and calling a function with arguments. He learns that passing can take one of two forms: pass by value or pass by reference.

Geek wishes to add 1 and 2, respectively, to the parameter passed by value and reference. Help Geek in fulfilling his goal.

Example 1:

Input:
a = 1
b = 2
Output:
2 4
Explanation: 1 was passed by value whereas 2 passed by reference.

Example 2:

Input:
a = 10
b = 20
Output: 11 22
Explanation: 10 was passed by value whereas 20 passed by reference.

Constraints:
1 <= a,b <= 105

Your Task:
You don't need to read input or print anything. Your task is to complete the function passedBy() which takes a and b as input parameters and returns array of two required integers.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> passedBy(int a, int &b) {
        return {a + 1 , b + 2};
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cout << "Enter two numbers" << endl;
        cin >> a >> b;
        Solution obj;
        vector<int> ans = obj.passedBy(a, b);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}
