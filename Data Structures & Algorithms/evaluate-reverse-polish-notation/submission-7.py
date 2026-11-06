class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_index = 0
        stack = []
        operations = {'+' : lambda x, y : x+y, '*' : lambda x, y : x*y,
                      '-' : lambda x, y : x-y, '/' : lambda x, y : int(x/y)}
        for token in tokens :
            if token in operations :
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](int(a), int(b)))
            else :
                stack.append(int(token))
        return int(stack[0])

                    
       
                

        