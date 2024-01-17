'''
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        
        
    def merge_sort(self,nums):    
        if len(nums)==1:
            return nums
        
        pivot=int(len(nums)//2)
        left_list=self.merge_sort(nums[:pivot])
        right_list=self.merge_sort(nums[pivot:])
        #print("LL and RL: ", left_list, right_list)
        return self.merge(left_list, right_list)
    
    
    def merge(self,left_list, right_list):
        merged=[]
        left_pointer=right_pointer=0
        while left_pointer<len(left_list) and right_pointer<len(right_list):
            if left_list[left_pointer] < right_list[right_pointer]:
                merged.append(left_list[left_pointer])
                left_pointer+=1
            else:
                merged.append(right_list[right_pointer])
                right_pointer+=1
        #print("merged: ", merged)        
       #append whatever is remaining in either of the lists
        merged.extend(left_list[left_pointer:])
        merged.extend(right_list[right_pointer:])
        
        return merged     
    
                
            
        