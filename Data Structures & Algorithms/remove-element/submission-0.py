class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr=0
            
        for i in range (0,len(nums)):
            # print(f"nums i= {i},curr ={curr} nums= {nums}")
            if nums[i]!=val:
                nums[curr]=nums[i]
                curr+=1
        # print("updated nums = ", nums)
        # print("index curr = ", curr)
        return curr
                
        