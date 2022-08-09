class MyQueue:

    def __init__(self):
        self.st = []
        self.st1 = []

    def push(self, x: int) -> None:
        self.st.append(x)
        
    def pop(self) -> int:
        while len(self.st)!=1:
            self.st1.append(self.st[-1])
            self.st.pop()
        res = self.st.pop()
        
        while len(self.st1)!=0:
            self.st.append(self.st1[-1])
            self.st1.pop()
            
        return res
    
    def peek(self) -> int:
        if len(self.st)!=0:
            return self.st[0]
        
    def empty(self) -> bool:
        if len(self.st)!=0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()