class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            curr_val = nums[index]

            for i in range(index+1, len(nums)):
                if curr_val + nums[i] == target:
                    return [index, i]
        
        