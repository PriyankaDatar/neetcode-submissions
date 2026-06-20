class Solution:
    stepsMap = {}
    def climbStairs(self, n: int) -> int:

        if n==1:
            return 1
        elif n==2:
            return 2 #1+1 or 2
        elif (n in self.stepsMap):
            return self.stepsMap[n]
        else:
            ans = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.stepsMap[n]=ans
            return ans
        



        # 3 -> 1+1+1 , 1+2, 2+1 -> (3)
        # 4 -> 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 (3+2)
        # 5 ->  1+ [climb(4)], 2+[climb[3]]-> 1+5+3=9 (5+3)
        # climb(n)=1+climb(n-1)+climb(n-2)