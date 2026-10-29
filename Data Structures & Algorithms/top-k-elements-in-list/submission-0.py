class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(tuple)
        for num in nums:
            if num not in frequency : 
                frequency[num] = (1, num)
            else : 
                frequency[num] = (frequency[num][0] + 1, num)
        return [num[1] for num in sorted(frequency.values(), reverse=True)][:k]
        