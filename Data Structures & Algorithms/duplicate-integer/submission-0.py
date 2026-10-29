class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # turn it into a hashset
        num_set = set(nums);
        
        # if nums of ele not equal -> contains duplicate
        return len(num_set) != len(nums)
        