class Solution:
   
    '''
approach  using boundary index  left and right
Binary search
input:sorted array(num) and a target value (target)to be searched
output:index of the target value
'''


    def search(self,num, target ) :
        left = 0  # lowerbound
        right = len(num)-1  # upperbound
        while (left <= right):  # while the index of list in range
            mid = (left + right) // 2
            if num[mid] == target:  # middle element is the target value
                return mid
            elif num[mid] > target: # if middle element is greater then cut rightmost part
                right = mid - 1
            else:  # if middle element is on right then cut the left most part
                left = mid + 1

        return -1  # if we don't find the target value
