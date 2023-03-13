'''
Problem - Rotated Lists
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times 
the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of
the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. 
E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

Logic For solving:

If the middle element is smaller than its predecessor, then it is the answer. However, if it isn't, this check is not sufficient to determine whether
the answer lies to the left or the right of it. Consider the following examples.
[7, 8, 1, 3, 4, 5, 6] (answer lies to the left of the middle element)
[1, 2, 3, 4, 5, -1, 0] (answer lies to the right of the middle element)

check that will help us determine if the answer lies to the left or the right: 
    1. If the middle element of the list is smaller than the last element of the range, then the answer lies to the left of it. 
    2. Otherwise, the answer lies to the right.
    
Algorithm:
Binary search Solution
    1. set the values of lo=0 and hi=len(nums)-1 and calculate the mid using( lo+hi)//2 
    2. check if mid is smaller than its predecessor ,if true return mid 
    3. else decide the left and right halve using a check with last element of the nums 
    4. if mid element is less than the last element then select the left halve with hi=mid-1 
    5. if mid element is greater than the last element then select the right halve with lo=mid+1 
    6. repeat step 2 to 5 till lo<= high and return 0 if no check was successful 
    
 nums:rotated list 
 lo:starting index
 hi:end index
 
 time complexity:O(logn)
 space complexity=O(1)
   
'''
def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    
    while lo<=hi:
        mid =(lo+hi)//2
        mid_number = nums[mid]

        if mid > 0 and nums[mid]<nums[mid-1]:
            # The middle position is the answer
            return mid
        
        elif nums[mid]<nums[len(nums)-1]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0
 
'''
Using generic binary search function

def count_rotations_generic(nums):
    def condition(mid):
        if mid>0 and nums[mid]<nums[mid-1]:
            return 'found'
        elif nums[mid]<nums[len(nums)-1]:
            return 'left'
        else:
            return 'right'
        
        
    return 0 if binary_search(0, len(nums)-1, condition)==-1 else binary_search(0, len(nums)-1, condition)
  
  def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
    
    '''


