class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0

        for fast in range(len(nums)):
            curr = nums[fast]

            if curr != val:
                nums[slow] = curr
                slow += 1
        
        return slow