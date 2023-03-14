'''
time complexity=O(logn)
space complexity=O(1)
'''
class position:
    
    def first_position(self,nums, target):
        def condition(mid):
            if nums[mid] == target:
                if mid > 0 and nums[mid-1] == target:
                    return 'left'
                return 'found'
            elif nums[mid] < target:
                return 'right'
            else:
                return 'left'
        return self.binary_search(0, len(nums)-1, condition)
    def last_position(self,nums, target):
        def condition(mid):
            if nums[mid] == target:
                if mid <len(nums)-1 and nums[mid+1] == target:
                    return 'right'
                return 'found'
            elif nums[mid] < target:
                return 'right'
            else:
                return 'left'
        return self.binary_search(0, len(nums)-1, condition)
    def binary_search(self,lo, hi, condition):
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
        
p=position()
print(p.first_position([5,5,5,5,5,6,6,6,9,10,15],6),
p.last_position([5,5,5,5,5,6,6,6,9,10,15],6))
