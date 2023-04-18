# link: https://leetcode.com/problems/trapping-rain-water/
# Time: O(n)
# Revision date: NA
###############----HINTS----####################
# hint: two pointers
# hint: use two pointers for index and two variables for left max and right max
# hint: aim is to calculate the water retained on top of each possible indices
# hint: move forward if left max is less than right max and calculate the new left max and vice-versa
# hint: update answer by calculating the water that will be retained on top of the new index (moved) based on its
#       respective maximum (left or right)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ml = height[l]
        mr = height[r]
        ans = 0
        while(l<r):
            if(height[l]>height[r]):
                r-=1
                mr = max(mr, height[r])
                ans+= mr - height[r]
            else:
                l+=1
                ml = max(ml, height[l])
                ans += ml - height[l]
        return ans