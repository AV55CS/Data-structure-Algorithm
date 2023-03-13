'''
Searching in a Rotated List
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.
Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.

nums:rotated list
target:value to be searched
lo:starting index
hi:end index

time complexity=O(logn)
space Comlexity =O(1)
'''

def find_element(nums,target):
    lo = 0
    hi = len(nums)-1
    while lo<=hi:
        mid =(lo+hi)//2
        if nums[mid]== target:
            return mid
		#whether the target is on the left halve
        elif target>nums[0]:
		   #if mid is on right 
            if nums[mid]<nums[0] or nums[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
        else:
		   #if mid is bigger then searching right halve
            if nums[mid]>nums[0] or nums[mid]<target:
                lo=mid+1
                
            else:
                hi=mid-1
            
        
    return -1            
