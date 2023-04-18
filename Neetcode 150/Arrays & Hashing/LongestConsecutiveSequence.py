# link: https://leetcode.com/problems/valid-anagram/
# Time: O(2n)
# Revision date: 22/1/23

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            if(n-1 not in hashset):
                length = 0
                while(n+length in hashset):
                    length+=1
                longest = max(longest, length)
        return longest