from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # Phase 1: Find a candidate for the majority element
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Phase 2: Since the problem guarantees a majority element,
        # we do not need to verify the candidate.
        
        return candidate
