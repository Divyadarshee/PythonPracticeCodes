# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time: O(n)
# Revision date: NA

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        ans = 0
        while(l<r):
            if(numbers[l]+numbers[r] == target):
                return [l,r]
            elif(numbers[l]+numbers[r]>target):
                r-=1
            else:
                l+=1
        return ans