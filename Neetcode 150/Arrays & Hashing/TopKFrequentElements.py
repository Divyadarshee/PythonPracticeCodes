# link: https://leetcode.com/problems/top-k-frequent-elements/
# Time: O(n)
# Revision date: NA
##############-------HINTS--------##################
# hint: map to store frequency of each number
# hint: convert map and store to a new array with fixed length of len(nums)+1
#       and store the values in the corresponding frequency index in the new array
# hint: iterate the new array in reverse order and add the values from the highest frequency till k is exhausted
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        count = [[] for i in range(len(nums)+1)]
        ans = list()
        for n in nums:
            hashmap[n]+=1
        for n, c in hashmap.items():
            count[c].append(n)
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                ans.append(n)
                if(len(ans) == k):
                    return ans