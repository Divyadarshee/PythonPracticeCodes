# link: https://leetcode.com/problems/permutation-in-string/
# Time: O(n)
# Revision date: NA

from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matched, substr_start, window_start = 0, 0, 0
        min_length = len(s)+1
        frequency_map = dict()

        for ch in t:
            if ch not in frequency_map:
                frequency_map[ch] = 0
            frequency_map[ch] += 1
        
        for window_end in range(len(s)):
            right = s[window_end]
            if right in frequency_map:
                frequency_map[right]-=1
                if(frequency_map[right]>=0):
                    matched+=1
            
            while(matched == len(t)):
                if(min_length>window_end-window_start+1):
                    min_length = window_end-window_start+1
                    substr_start = window_start
                left = s[window_start]
                window_start+=1
                if(left in frequency_map):
                    if(frequency_map[left]==0):
                        matched-=1
                    frequency_map[left]+=1
        if min_length > len(s):
            return ""
        return s[substr_start:substr_start+min_length]

