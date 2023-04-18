# hint:

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        matched = 0
        hm = dict()
        for ch in s1:
            if ch not in hm:
                hm[ch] = 0
            hm[ch]+=1

        for r in range(len(s2)):
            ch = s2[r]
            if ch in hm:
                hm[ch]-=1
                if(hm[ch] == 0):
                    matched +=1

            if(r-l+1>len(s1)):
                left = s2[l]
                l+=1
                if(left in hm):
                    if(hm[left] == 0):
                        matched -=1
                    hm[left]+=1
            if(matched == len(hm)):
                return True
        return False

a = Solution()
print(a.checkInclusion("abcdxabcde", "abcdeabcdx"))



# # hint: sliding window
# # hint: map for the characters and their frequencies
# # hint: all we need for checking our constraint is the number of non max_frequent character
# # hint: condition:
# #       simpler -> r-l+1-max(count.values())>k
# #        complex -> window_end - window_start + 1 - max_frequency
# # hint: while the constraint is not satisfied move the left boundary to right (slide)
# # IMP: read the reason for the not requiring the decrement of max_frequency value
#
# from typing import List
#
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         window_start = 0
#         frequency_map = dict()
#         max_frequency = 0
#         frequent_element = ""
#
#         for window_end in range(len(s)):
#             ch = s[window_end]
#             if ch not in frequency_map:
#                 frequency_map[ch] = 0
#             frequency_map[ch]+=1
#             if(max_frequency<frequency_map[ch]):
#                 max_frequency = frequency_map[ch]
#                 frequent_element = ch
#             if (window_end - window_start + 1 - max_frequency > k):
#                 left = s[window_start]
#                 window_start += 1
#                 frequency_map[left] -= 1
#             ans = max(ans, window_end - window_start + 1)
#         return ans
#
#
# class Solution:
#     def characterReplacement(self, s : str) -> int:
#         l = 0
#         count = dict()
#         max_frequency = 0
#
#         for r in range(len(s)):
#             count[s[r]] = count.get(s[r], 0) + 1
#             max_frequency = max(count[s[r]], max_frequency)
#
#             while(r-l+1-max_frequency>k):
#                 left = s[l]
#                 count[left] -= 1
#                 l+=1
#
#             ans = max(r-l+1, ans)




# # hint: sliding window
# # hint: use a set for the window
# # hint:
#
# from typing import List
#
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         window = set()
#         window_left = 0
#         ans = 0
#
#         for window_end in range(len(s)):
#             ch = s[window_end]
#             if (ch not in window):
#                 window.add(ch)
#             else:
#                 while (ch in window):
#                     window.remove(s[window_left])
#                     window_left += 1
#                 window.add(ch)
#                 ans = max(ans, len(window))
#
#         return ans
#
#
# a = Solution()
# print(a.lengthOfLongestSubstring("bacabcbb"))

# # hint: two pointers
# # hint: use two pointers for index and two variables for left max and right max
# # hint: aim is to calculate the water retained on top of each possible indices
# # hint: move forward if left max is less than right max and calculate the new left max and vice-versa
# # hint: update answer by calculating the water that will be retained on top of the new index (moved) based on its
# #       respective maximum (left or right)
#
# from typing import List
#
#
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l = 0
#         r = len(height) - 1
#         ml = height[l]
#         mr = height[r]
#         ans = 0
#         while (l < r):
#             if (ml < mr):
#                 l += 1
#                 ml = max(ml, height[l])
#                 ans += ml - height[l]
#
#             else:
#                 r -= 1
#                 mr = max(mr, height[r])
#                 ans += mr - height[r]
#
#         return ans
#
#
# a = Solution()
# print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# # hint: keep it simple
# # hint: dont confuse this with trapping rain water question
# # hint: two pointers
#
# from typing import List
#
#
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l = 0
#         r = len(height)-1
#         ans = 0
#         while(l<r):
#             ans = max(ans, min(height[l], height[r])*(r-l))
#             if(height[l]<height[r]):
#                 l+=1
#             else:
#                 r-=1
#         return ans
#
# a = Solution()
# print(a.maxArea([1,8,6,2,5,4,8,3,7]))
# print(a.maxArea([1,1]))


# # hint: sort the input array
# # hint: take the first element via a loop and look for the next two numbers using two pointers method
# # to solve the unique solutions constraint below "hints"
# # hint: while taking the first number of thw threesum make it is not same as the previous one
# # hint: once you find a solution after appending to the final list increment one pointer and keep doing so until the next
# #       pointer points to a unique number as compared to the one inserted in the final list of solutions
# # to improve the time complexity a little bit
# # hint: once the main loop reached a number > 0 break - reason since all the numbers are in sorted order not possible to
# #       get 0 with the least number being positive (>0)
#
# from typing import List
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans = []
#         for i in range(len(nums)-2):
#             if(i>0 and nums[i-1]==nums[i]):
#                 continue
#             a = nums[i]
#             l = i+1
#             r = len(nums)-1
#             while(l<r):
#                 curr = a + nums[l] + nums[r]
#                 if(curr < 0):
#                     l+=1
#                 elif(curr>0):
#                     r-=1
#                 else:
#                     ans.append([a, nums[l], nums[r]])
#                     l+=1
#                     while(l<r and nums[l-1] == nums[l]):
#                         l+=1
#         return ans
#
# a = Solution()
# print(a.threeSum([0,0,0,0]))

# # hint: incremental length checking
# # hint: set
# # hint: find the starting of each consecutive sequence
# # hint: Above starting point is defined by the characteristic of not having a number previous to it
# # hint: from the starting point start a loop finding the next element and increment the length and compare
# #       to store the longest one
# from typing import List
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numset = set(nums)
#         ans = 0
#         for n in numset:
#             if(n-1 not in numset):
#                 l = 1
#                 while(n + l in numset):
#                     l+=1
#                 ans = max(ans, l)
#         return ans
#
#
# a = Solution()
# print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

# # hint: set for each checking features - row, column, sub-board(3X3)
# # hint: use key for sub-board as row//3, col//3
# # hint: use default dict
# # Remember: dictonary can only take tuple as the key and not a list
# from typing import List
# from collections import defaultdict
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         row = defaultdict(set)
#         col = defaultdict(set)
#         block = defaultdict(set)
#
#         for r in range(9):
#             for c in range(9):
#                 item = board[r][c]
#                 if(item == '.'):
#                     continue
#                 if(item in row[r] or item in col[c] or item in block[(r//3, c//3)]):
#                     return False
#                 row[r].add(item)
#                 col[c].add(item)
#                 block[(r//3, c//3)].add(item)
#         return True
#
# a = Solution()
# print(a.isValidSudoku([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))


# hint: pre and post
# class Solution:
#     def productExceptSelf(self, nums):
#         ans = [1]*len(nums)
#         pre = 1
#         post = 1
#         for i in range(len(nums)):
#             ans[i] *= pre
#             pre *= nums[i]
#             ans[len(nums) - 1 - i] *= post
#             post *= nums[len(nums)-1-i]
#         return ans
#
# a = Solution()
# print(a.productExceptSelf([1,2,3,4]))


# # hint: map to store frequency of each number
# # hint: convert map and store to a new array with fixed length of len(nums)+1
# #       and store the values in the corresponding frequency index in the new array
# # hint: iterate the new array in reverse order and add the values from the highest frequency till k is exhausted
# class Solution:
#     def topKFrequent(self, nums, k):
#         hm = dict()
#         count = [[] for i in range(len(nums)+1)]
#         for n in nums:
#             if n not in hm:
#                 hm[n]=0
#             hm[n]+=1
#         print(hm)
#         cm = dict()
#         for i, v in enumerate(hm):
#             count[hm[v]].append(v)
#         ans = []
#         for i in range(len(count)-1,-1,-1):
#             for n in count[i]:
#                 ans.append(n)
#                 k-=1
#                 if k == 0:
#                     return ans
#         return ans
#
#
# a = Solution()
# print(a.topKFrequent([1],1))


# # hint: count of each character frequency
# # hint: count is the key for the map
# # hint: only tuple can be used as a key and not a list
# import collections
#
#
# class Solution:
#     def groupAnagrams(self, strs):
#         hm = collections.defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for ch in s:
#                 count[ord(ch) - ord('a')] += 1
#             hm[tuple(count)].append(s)
#
#         return hm.values()
#
#
# a = Solution()
# print(list(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
