class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=m+n-1

        while(i>=0 and j>=0):
            while(j>=0 and i>=0 and nums2[j]>nums1[i]):
                nums1[k]=nums2[j]
                j=j-1
                # i=i-1
                k=k-1
            while(i>=0 and j>=0 and nums1[i]>=nums2[j]):
                temp=nums1[k]
                nums1[k]=nums1[i]
                nums1[i]=temp
                i=i-1
                k=k-1
            # while(j>=0 and i>=0 and nums2[j]>=nums1[i]):
            #     nums1[k]=nums2[j]
            #     j=j-1
            #     k=k-1
        while(j>=0 and k>=0):
            nums1[k]=nums2[j]
            j=j-1
            k=k-1
        # print(nums1,i,j,k )
            
        

        

        