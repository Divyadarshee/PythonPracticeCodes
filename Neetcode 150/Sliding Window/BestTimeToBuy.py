# link: https://leetcode.com/problems/container-with-most-water/
# Time: O(n)
# Revision date: NA

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        ans = 0
        for r in prices:
            lowest = min(lowest, r)
            ans = max(ans, r-lowest)
        return ans