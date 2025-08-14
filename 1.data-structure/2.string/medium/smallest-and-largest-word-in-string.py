"""
Given a string, find the minimum and the maximum length words in it.
Examples:

Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string
Input : "GeeksforGeeks A computer Science portal for Geeks"
Output : Minimum length word: A
         Maximum length word: GeeksforGeeks

"""


class Solution:
    def smallest_and_largest_word_in_string(self, s):
        local_min_len = float("inf")
        local_min_end = None
        local_max_len = -float("inf")
        local_max_end = None

        # Iterate over the string and for each encounter of space, updating the smallest and largest word
        word_tracker = 0
        for i, char in enumerate(s):
            if char == " " and word_tracker > 0:
                if word_tracker > local_max_len:
                    local_max_len = word_tracker
                    local_max_end = i - 1
                if word_tracker < local_min_len:
                    local_min_len = word_tracker
                    local_min_end = i - 1
                word_tracker = 0
            else:
                word_tracker += 1

        # Update of smallest or largest word for the last word of string
        if word_tracker > 0:
            if word_tracker > local_max_len:
                local_max_len = word_tracker
                local_max_end = i
            if word_tracker < local_min_len:
                local_min_len = word_tracker
                local_min_end = i
            word_tracker = 0

        result = []
        # Creation of smallest and largest word using end index and len of words
        temp_str = ""
        for i in range(local_min_end - local_min_len + 1, local_min_end + 1):
            temp_str += s[i]
        result.append(temp_str)
        temp_str = ""
        for i in range(local_max_end - local_max_len + 1, local_max_end + 1):
            temp_str += s[i]
        result.append(temp_str)
        return result


def main():
    s = input("Enter a sentence: ").strip()
    solution = Solution()
    print(solution.smallest_and_largest_word_in_string(s))


if __name__ == "__main__":
    main()
