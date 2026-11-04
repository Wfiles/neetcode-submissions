class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        set_num = set(nums)
        for num in set_num:
            curr_sequence = 1
            curr_num = num
            if num - 1 not in set_num:
                while curr_num + 1 in set_num:
                    curr_num = curr_num + 1
                    curr_sequence += 1
            longest_sequence = max(curr_sequence, longest_sequence)
        return longest_sequence


                
            
        