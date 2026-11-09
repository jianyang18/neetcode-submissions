class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2

        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1

            if (num_count[num] > target):
                return num
        