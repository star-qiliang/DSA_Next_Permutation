class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        tmp = None
        for j in range(len(nums)-1,0,-1):
            if nums[j-1]<nums[j]:
                for j2 in range(len(nums)-1,j-1,-1):
                    if nums[j-1]<nums[j2]:
                        if j2+1<len(nums):
                            if nums[j2+1]<nums[j-1]:
                                tmp=nums[j-1]
                                nums[j-1] = nums[j2]
                                nums[j2] = tmp
                            else:
                                pass
 
                        else:
                            tmp=nums[j-1]
                            nums[j-1] = nums[j2]
                            nums[j2] = tmp
                    else:
                        pass

            else:
                pass

