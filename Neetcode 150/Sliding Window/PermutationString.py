# link: https://leetcode.com/problems/permutation-in-string/
# Time: O(n)
# Revision date: NA

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_map = dict()

        for ch in s1:
            if ch not in frequency_map:
                frequency_map[ch] = 0
            frequency_map[ch]+=1
        window_start = 0
        matched = 0
        for window_end in range(len(s2)):
            right = s2[window_end]
            if right in frequency_map:
                frequency_map[right]-=1
                if(frequency_map[right] == 0):
                    matched+=1
            
            if(matched == len(frequency_map)):
                return True
            
            if(window_end-window_start+1 >= len(s1)):
                left = s2[window_start]
                window_start+=1
                if(left in frequency_map):
                    if(frequency_map[left]==0):
                        matched -=1
                    frequency_map[left]+=1
        return False
