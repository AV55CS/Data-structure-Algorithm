'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.


Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
    

'''

def searchInsert(self, nums: List[int], target: int) -> int:
        left=0 #lower bound
        right=len(nums)#length of nums
        while(left<right):#we need to search the position thats why < sign
            mid=(left+right)//2 #calculating the middle 
            if nums[mid]<target: #if target is less than  middle
                left=mid+1
            else:
                right=mid
        

        return left
