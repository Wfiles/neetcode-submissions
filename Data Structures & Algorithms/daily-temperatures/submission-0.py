class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures) :
            if len(stack) == 0 :
                stack.append(i)
                continue
            while len(stack) != 0 and temperature > temperatures[stack[len(stack) - 1]] :
                temp_index = stack.pop()
                result[temp_index] = i - temp_index
            stack.append(i)
        return result

                
        
            




        