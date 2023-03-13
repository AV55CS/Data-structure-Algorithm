'''
index():function returns index of the value inside the list if found else returns 'ValueError'.
try:try block is used to  test a block of code for errors.
except:except block is used to  handle the error

time complexity=O(n)
space complexity=O(1)
'''

def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            x=nums.index(target)
            for i in range(x,len(nums),1):
                    if nums[i]==target:
                        x=x+1
                        continue
            return [nums.index(target),x-1]
        except ValueError:
            return  [-1,-1]
