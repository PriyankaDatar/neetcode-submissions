class MinStack:
    min_stack=None
    min_val=None
    mapping = None


    def __init__(self):
        self.min_stack=[]
        self.min_val=None
        self.mapping = {}
        

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if self.min_val==None:
            self.min_val=val
            self.mapping[self.min_val]=None
        elif self.min_val>= val:
            new = self.mapping.get(val,[])
            if new==None:
                new = [self.min_val]
            else:
                new.extend([self.min_val])
            self.mapping[val]=new
            self.min_val=val
        

    def pop(self) -> None:
        ele = self.min_stack.pop() #removes last element of the list
        if ele==self.min_val:
            #recompute min_val? 
            if self.mapping[ele] and len(self.mapping[ele])>0:
                self.min_val= self.mapping[ele].pop()
            else:
                self.min_val= None

    def top(self) -> int:
        top_ele = self.min_stack[-1]
        return top_ele

    def getMin(self) -> int:
        print("min = ",self.min_val)
        return self.min_val
