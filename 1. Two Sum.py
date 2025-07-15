from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in pairs.keys():
                return [pairs[needed], i]
            pairs[nums[i]] = i


print(Solution().twoSum([2,7,11,15], 9))
