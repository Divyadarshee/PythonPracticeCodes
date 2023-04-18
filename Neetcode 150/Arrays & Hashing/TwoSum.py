# link: https://leetcode.com/problems/two-sum/
# Time: O(n)
# Revision date: NA

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            if(target-nums[i] in hashmap):
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i
        return []
        