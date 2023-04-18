# link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Time: O(n)
# Revision date: NA
###############----HINTS----####################
# hint: sliding window
# hint: map for the characters and their frequencies
# hint: all we need for checking our constraint is the number of non max_frequent character
# hint: condition:
#       simpler -> r-l+1-max(count.values())>k
#        complex -> window_end - window_start + 1 - max_frequency
# hint: while the constraint is not satisfied move the left boundary to right (slide)


# IMP: read the reason for the not requiring the decrement of max_frequency value

from typing import List


# most optimized solution
# O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = dict()
        max_frequency = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_frequency = max(count[s[r]],
                                max_frequency)  # -> reason for not decrementing this value
            # when we slide the window (remove the leftmost character):
            # 1. the next bigger answer(result) will be only when the max_frequency increases
            # 2. we want our answer to be max which means we want our window length to be max which also needs the
            #    max_frequency to increase so having an overestimated max_frequency allows to find the new answer

            while (r - l + 1 - max_frequency > k):
                left = s[l]
                count[left] -= 1
                l += 1

            ans = max(r - l + 1, ans)

# non-optimized solution of above
# O(26n)
# class Solution:
#     def characterReplacement(self, s : str) -> int:
#         l = 0
#         count = dict()

#         for r in range(len(s)):
#             count[s[r]] = count.get(s[r], 0) + 1

#             while(r-l+1-max(count.values())>k):
#                 left = s[l]
#                 count[left] -= 1
#                 l+=1

#             ans = max(r-l+1, ans)


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         frequency_map = dict()
#         max_frequency = 0
#         max_frequent_character = ""
#         window_start = 0
#         for r in range(len(s)):
#             right = s[r]
#             if right not in frequency_map:
#                 frequency_map[right] = 0
#             frequency_map[right]+=1
#             if(frequency_map[right]>max_frequency):
#                 max_frequency = frequency_map[right]
#                 max_frequent_character = right
#             if(r-window_start+1-max_frequency>k):
#                 left = s[window_start]
#                 window_start+=1
#                 frequency_map[left]-=1
#             ans = max(ans, r-window_start+1)
#         return ans
