class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in compliment:
                return [compliment.get(needed), i]
            compliment[nums[i]] = i
        
        return