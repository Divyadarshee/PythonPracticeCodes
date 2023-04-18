# link: https://leetcode.com/problems/contains-duplicate/
# Time: O(n)
# Revision date: NA

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Method-1
        # Using dictionary
        hashmap = dict()

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                return True
        return False

        # Method-2
        # Using set
        ###
        numset = set(nums)
        return len(nums) == len(numset)
        ###

