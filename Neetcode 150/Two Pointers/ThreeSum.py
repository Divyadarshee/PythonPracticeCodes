# link: https://leetcode.com/problems/3sum/
# Time: O(n)
# Revision date: NA
###############----HINTS----####################
# hint: sort the input array
# hint: take the first element via a loop and look for the next two numbers using two pointers method
# to solve the unique solutions constraint below "hints"
# hint: while taking the first number of thw threesum make it is not same as the previous one
# hint: once you find a solution after appending to the final list increment one pointer and keep doing so until the
#        next pointer points to a unique number as compared to the one inserted in the final list of solutions
# to improve the time complexity a little bit
# hint: once the main loop reached a number > 0 break - reason since all the numbers are in sorted order not possible to
#       get 0 with the least number being positive (>0)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, n in enumerate(nums):
            if(n>0):
                break
            if(i>0 and nums[i-1] == nums[i]):
                continue
            l = i+1
            r = len(nums)-1
            while(l<r):
                s = n+nums[l]+nums[r]
                if(s==0):
                    ans.append([n,nums[l],nums[r]])
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
                elif(s>0):
                    r-=1
                else:
                    l+=1
            
        return ans