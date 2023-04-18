# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time: O(n)
# Revision date: NA

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        window_start = 0
        ans  = 0
        for window_end in range(len(s)):
            right = s[window_end]
            while(right in window):
                window.remove(s[window_start])
                window_start += 1
            window.add(right)
            ans = max(ans, len(window))
        return ans
