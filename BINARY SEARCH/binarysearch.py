 '''
approach  using boundary index  left and right
Binary search
input:sorted array(num) and a target value (target)to be searched
output:index of the target value
'''


    def search(self,num, target ) :
      # lowerbound
        left = 0  
        # upperbound
        right = len(num)-1  
         # while the index of list in range
        while (left <= right): 
            mid = (left + right) // 2
            # middle element is the target value
            if num[mid] == target: 
                return mid
             # if middle element is greater then cut rightmost part
            elif num[mid] > target: 
                right = mid - 1
             # if middle element is on right then cut the left most part
            else: 
                left = mid + 1
                
         # if we don't find the target value
        return -1 
