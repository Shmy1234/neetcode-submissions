class MinStack:
    
    def __init__(self):
        self.lst = []

    def push(self, val: int) -> None:
        self.lst.append(val)

    def pop(self) -> None:
        if len(self.lst) != 0:
            self.lst.pop()
        
    def top(self) -> int:
        return self.lst[-1]
        
    def getMin(self) -> int:
        return min(self.lst) 

        
