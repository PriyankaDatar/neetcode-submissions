class Solution:
    def isValid(self, s: str) -> bool:
        myStack =[]
        mapping ={']':'[', '}':'{', ')':'('}
        for c in s:
            if c in ['[', '{','(']:
                myStack.append(c)
            elif c in [']','}',')']:
                if len(myStack)==0:
                    return False
                tos = myStack[-1]
                if tos==mapping[c]:
                    myStack.pop()
                else:
                    return False
        return len(myStack)==0
        