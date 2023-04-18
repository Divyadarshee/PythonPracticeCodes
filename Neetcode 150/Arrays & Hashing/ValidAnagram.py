# link: https://leetcode.com/problems/valid-anagram/
# Time: O(n)
# Revision date: NA

from typing import List


class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()

        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 0
            hashmap[ch]+=1
        for ch in t:
            if ch in hashmap:
                hashmap[ch]-=1
                if(hashmap[ch]==0):
                    hashmap.pop(ch)
                else:
                    return False
        return len(hashmap)==0