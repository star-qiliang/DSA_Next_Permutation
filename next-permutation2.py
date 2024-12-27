class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)-1,0,-1):  # j>=1
            # print("j:", j)
            if nums[j-1]<nums[j]:
                for j2 in range(len(nums)-1,j-1,-1): # j2>=j
                    # print("j2:", j2)
                    if nums[j-1]<nums[j2]:
                        if j2+1<len(nums):
                            if nums[j2+1]<=nums[j-1]:
                                tmp=nums[j-1]
                                nums[j-1] = nums[j2]
                                nums[j2] = tmp

                                k=j
                                # l=j2
                                l=len(nums)-1
                                while(k<l):
                                    # print("k:", k)
                                    # print("l",l)
                                    tmp = nums[k]
                                    nums[k] = nums[l]
                                    nums[l] = tmp
                                    k+=1
                                    l-=1

                                return
                            else:
                                # print('pass 1')
                                pass
 
                        else:
                            tmp=nums[j-1]
                            nums[j-1] = nums[j2]
                            nums[j2] = tmp
                            # print("j2:", j2)

                            k=j
                            # l=j2
                            l=len(nums)-1
                            while(k<l):
                                # print("k:", k)
                                # print("l",l)
                                tmp = nums[k]
                                nums[k] = nums[l]
                                nums[l] = tmp
                                k+=1
                                l-=1
                            return
                    else:
                        # print("pass 2")
                        pass

            else:
                # print("pass 3")
                pass

        i=0
        j=len(nums)-1
        while(i<j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i+=1
            j-=1

        return

