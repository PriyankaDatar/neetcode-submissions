class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_length=2*len(nums)
        new_nums=[0]* new_length
        for i in range(len(nums)):
            new_nums[i]=nums[i]
            new_nums[i+len(nums)]=nums[i]
        return new_nums


        