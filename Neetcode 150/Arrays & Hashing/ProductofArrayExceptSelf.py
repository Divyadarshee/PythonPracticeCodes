# link: https://leetcode.com/problems/product-of-array-except-self/
# Time: O(n)
# Space: O(1)
# Revision date: NA
###############----HINTS----####################
# hint: count of each character frequency

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        ans = [1 for i in range(len(nums))]
        length = len(nums)-1
        for i in range(len(nums)):
            ans[i] *=prefix
            prefix *= nums[i]
            ans[length -i] *= suffix
            suffix *= nums[length - i]
        return ans