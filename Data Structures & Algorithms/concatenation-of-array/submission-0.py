class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * 2 * n

        for index, value in enumerate(nums):
            res[index] = res[index + n] = value
        
        return res