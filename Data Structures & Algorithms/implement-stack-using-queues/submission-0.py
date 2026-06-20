class MyStack:

    def __init__(self):
        self.q1= deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if len(self.q1)==0 and len(self.q2)==0:
            self.q1.append(x)
        else:
            self.q1.append(x)
            while len(self.q2)!=0:
                ele = self.q2.popleft()
                self.q1.append(ele)
        temp=self.q1
        self.q1=self.q2
        self.q2=temp

    def pop(self) -> int:
        return self.q2.popleft()

    def top(self) -> int:
        return self.q2[0] 

    def empty(self) -> bool:
        if len(self.q1)==0 and len(self.q2)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()