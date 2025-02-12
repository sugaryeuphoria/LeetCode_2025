"""
2185. Counting Words With a Given Prefix
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
"""
class Solution(object):
    def prefixCount(self, words, pref):
        # Initialize a counter to keep track of the number of words with the prefix
        count = 0
        # Loop through each word in the given list 'words'
        for word in words:
            # Check if the current word starts with the given prefix 'pref'
            if word.startswith(pref):
                # Increment the counter if the word starts with the prefix
                count += 1
                # Return the final count of words that start with the prefix
        return count