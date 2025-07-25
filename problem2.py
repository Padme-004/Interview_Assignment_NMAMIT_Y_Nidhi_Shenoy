# Question 2)	
# Given an array of integers, you need to rearrange it such that all zeroes are shifted to the end of the array																		
# The relative order of the non-zero elements must remain unchanged. This operation must be performed in-place, without creating a new copy of the array.																		

#Approach 1
def moveZeroes1(nums) -> None:
        i=0
        while i<len(nums):
            if nums[i]==0:
                j=i+1
                while j<len(nums) and nums[j]==0:
                    j+=1
                if j==len(nums):
                    break
                nums[i],nums[j]=nums[j],nums[i]
            i+=1

"""
So when I saw the question, the first approach which immediately came to mind was two pointers. If relative order didn't matter I could start j from the last index. But since I want the relative order of non-zero elements to be preserved, I should start the second pointer j from i+1. This solution satisfies the in-place sorting constraint with O(1) space. 
The idea used is that if a number at i in nums is zero, then I will find the first non-zero element starting from i+1. Then I will swap them. I have to make sure that I don't exceed the array's existing length doing this. But the time complexity of this approach is O(n^2) due to the nested while loops. 

While trying to think of a one pass solution, I thought that another way of achieving the same is if I shift any non-zero element that occurs immediately after a bunch of zeroes (or a single zero), to the left of the zero bunch (or single zero). This is not two pointer, but it lets me improve the time complexity to one pass O(n) and does not violate the in place condition. I remember solving this in Java and thinking that it is kind of like inching the zeroes towards the end of the array.
"""

#Approach 2
def moveZeroes2(nums) -> None:
    zeroes=0
    for i in range(len(nums)):
        if nums[i]==0:
            zeroes+=1
        else:
            if zeroes>0:
                nums[i-zeroes]=nums[i]
                nums[i]=0

             
        