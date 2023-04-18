# link: https://leetcode.com/problems/group-anagrams/
# Time: O(n)
# Revision date: NA
###############----HINTS----####################
# hint: count of each character frequency
# hint: count is the key for the map
# hint: only tuple can be used as a key and not a list

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            count = [0 for i in range(26)]
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            hashmap[tuple(count)].append(string)
        return list(hashmap.values())
