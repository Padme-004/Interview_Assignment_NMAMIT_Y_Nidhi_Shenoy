# Question 1)
# Given an array of integers, determine if any integer appears at least twice within the array. 										
# If such a duplicate exists, return true. If every element in the array is unique, return false.										

#Approach 1:
from collections import defaultdict
def containsDuplicate1(nums) -> bool:
        count=defaultdict(int)
        for num in nums:
            if count[num]==1:
                    return True
            count[num]+=1
        return False


"""
The first idea that sprang to mind instantly on seeing the question was to keep a count of each element and to return True if the element was seen prior to this. I immediately coded Approach 1 as shown above. This approach allows me to get to the solution within one pass so I can say it has a time complexity of O(n). Since I am using a dictionary, I have a space complexity of O(n) too. 

But as soon as I was done with this I remembered sets. That will be even more convenient because of its property of not allowing duplicates. Even though the time and space complexity remain the same as that of Approach 1, I can bypass the initial defaultdict initialization. I am also using the no duplicates property of sets so I am happier with this second approach.
"""
#Approach 2
def containsDuplicate2(nums) -> bool:
        nums_so_far=set()
        for num in nums:
            if num in nums_so_far:
                  return True
            nums_so_far.add(num)
        return False