class MinStack:

    def __init__(self):
        self.min_index = []
        self.main_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if len(self.main_stack) == 1:
            self.min_index.append(0)
        else:
            min_index = self.min_index[len(self.min_index) - 1]
            if val <= self.main_stack[min_index]:
                self.min_index.append(len(self.main_stack) - 1)

    def pop(self) -> None:
        self.main_stack.pop()
        if self.min_index[len(self.min_index) - 1] == len(self.main_stack):
            self.min_index.pop()
           

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.main_stack[self.min_index[len(self.min_index) - 1]]
        
