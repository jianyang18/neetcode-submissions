class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # let's use hash map babe
        h_map = dict()

        for index, value in enumerate(nums):
            rest = target - value
            if rest in h_map:
                return [h_map.get(rest), index]

            h_map[value] = index
        
