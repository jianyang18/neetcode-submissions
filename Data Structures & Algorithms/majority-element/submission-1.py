class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for num in nums:
            # case 1: num is res (+1)
            if num == res:
                count += 1

            # case 2: num is not res but count > 0 (-1)
            else:
                if count > 0:
                    count -= 1

            # case 3: num is not res and count == 0 (change res)
                else:
                    res = num
                    count += 1
        
        return res