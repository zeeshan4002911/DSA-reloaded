"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        hash_map = {}
        for ele in strs:
            hash_token = self.custom_hash_func(ele)
            if hash_token not in hash_map:
                hash_map[hash_token] = []
            hash_map[hash_token].append(ele)

        for hash_token in hash_map:
            result.append(hash_map[hash_token])
        return result

    def custom_hash_func(self, word):
        """
        Input: eat ; output: a1e1t1
        """
        hash_store = [0] * 26
        for ele in word:
            if str(ele).isascii():
                ascii_diff = ord(ele) - ord("a")
                if 0 <= ascii_diff < 26:
                    hash_store[ascii_diff] += 1
                else:
                    return None
            else:
                return None

        hash_str = ""
        for i, cnt in enumerate(hash_store):
            letter = chr(i + ord("a"))
            if cnt > 0:
                hash_str += letter + str(cnt)

        return hash_str


def main():
    strs = input("Enter the list of strings: ").strip().replace(",", " ").split()
    print(Solution().group_anagrams(strs))


if __name__ == "__main__":
    main()
