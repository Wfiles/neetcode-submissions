class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i, num in enumerate(nums) : 
            if not num in sum_dict :
                sum_dict[target - num] = i
            else : 
                return [sum_dict[num], i]
        