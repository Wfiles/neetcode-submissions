class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conversion_dict = {'(' : ')', '{' : '}', '[' : ']'}
        for char in s:
            if char in conversion_dict.values():
                if len(stack) == 0:
                    return False
                popped = stack.pop() 
                if conversion_dict[popped] != char :
                    return False
            else:
                stack.append(char)
        return len(stack) == 0 