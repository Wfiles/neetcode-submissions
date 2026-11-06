class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = sorted(range(len(position)), key=lambda k: position[k], reverse=True)
        stack = []
        for i in sorted_positions :
            moves_remaining = (target - position[i]) / speed[i]
            if len(stack) == 0 :
                stack.append(moves_remaining)
            elif stack[-1] < moves_remaining : 
                stack.append(moves_remaining)
        return len(stack)


             
        